"""Labwork 6a: plot y = 2x + sin^2(x) + 3 on [-5, 5] with matplotlib."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT_DIR = Path(__file__).resolve().parent

x = np.linspace(-5, 5, 500)
y = 2 * x + np.sin(x) ** 2 + 3

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, color="tab:blue", label=r"$y = 2x + \sin^2(x) + 3$")
ax.grid(True)
ax.set_title("hello, po!")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

fig.savefig(OUT_DIR / "po.pdf")
plt.show()
