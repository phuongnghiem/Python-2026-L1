"""Persistence: pickle + gzip compression, written by a background thread.

- load()            : read students.dat (gzip -> pickle) at start-up
- BackgroundSaver   : a worker thread that pickles, compresses and writes the data,
                      so the menu never waits for the disk.
"""
import copy
import gzip
import os
import pickle
import queue
import threading
import time
from pathlib import Path

# Always next to this script, whatever the current directory is.
ARCHIVE = Path(__file__).resolve().parent / "students.dat"


def load():
    """Return the School stored in students.dat, or None if missing/unreadable."""
    if not ARCHIVE.exists():
        return None
    try:
        with gzip.open(ARCHIVE, "rb") as f:
            return pickle.load(f)  # only load files written by this program
    except (OSError, EOFError, pickle.UnpicklingError, AttributeError, ImportError):
        return None


class BackgroundSaver:
    """Producer/consumer: the main thread queues snapshots, one worker thread saves them."""

    def __init__(self):
        self._queue = queue.Queue()
        self._thread = None
        self._lock = threading.Lock()
        self._status = "nothing saved yet"

    @property
    def status(self):
        with self._lock:
            return self._status

    def _set_status(self, text):
        with self._lock:
            self._status = text

    def start(self):
        if self._thread is None:
            self._thread = threading.Thread(target=self._worker, name="saver", daemon=True)
            self._thread.start()

    def request(self, school):
        """Called from the main thread; returns immediately.

        A deep copy is queued so the worker pickles a consistent snapshot even if the
        user keeps editing the data while the save is running.
        """
        self.start()
        self._set_status("saving in background...")
        self._queue.put(copy.deepcopy(school))

    def close(self, timeout=10):
        """Wait for pending saves to finish (call before the program exits)."""
        if self._thread is None:
            return
        self._queue.put(None)  # sentinel: stop the worker
        self._thread.join(timeout)

    def _worker(self):
        while True:
            snapshot = self._queue.get()
            if snapshot is None:
                break
            try:
                data = gzip.compress(pickle.dumps(snapshot))  # pickle + compression, off the main thread
                tmp = ARCHIVE.with_suffix(".tmp")
                tmp.write_bytes(data)
                os.replace(tmp, ARCHIVE)  # atomic: never leaves a half-written students.dat
                name = threading.current_thread().name
                self._set_status(f"saved at {time.strftime('%H:%M:%S')} by thread '{name}'")
            except Exception as error:  # keep the worker alive, just report
                self._set_status(f"save failed: {error}")


saver = BackgroundSaver()
