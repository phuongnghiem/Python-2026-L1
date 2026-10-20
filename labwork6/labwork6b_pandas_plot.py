"""Labwork 6b: plot student scores (scores.csv) with pandas + matplotlib."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DIR = Path(__file__).resolve().parent
COURSES = ["math", "python", "database"]

# load scores.csv into a data frame (missing scores stay NaN and are skipped by the plots)
scores = pd.read_csv(DIR / "scores.csv")

# 1. Scatter plot of math, python, db scores -> scattered.png
#    x = student, y = score, one colour per course
fig, ax = plt.subplots(figsize=(11, 5))
for course, color in zip(COURSES, ["tab:blue", "tab:orange", "tab:green"]):
    ax.scatter(scores["student_id"], scores[course], label=course, color=color)
ax.set_title("Student scores by course")
ax.set_xlabel("student_id")
ax.set_ylabel("score")
ax.tick_params(axis="x", rotation=90)
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()
fig.savefig(DIR / "scattered.png", dpi=150)

# 2. Histogram of each course's marks on 3 separate subplots -> histo.png
fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=True)
for ax, course in zip(axes, COURSES):
    ax.hist(scores[course].dropna(), bins=8, edgecolor="black")
    ax.set_title(course)
    ax.set_xlabel("score")
axes[0].set_ylabel("number of students")
fig.suptitle("Histogram of marks per course")
fig.tight_layout()
fig.savefig(DIR / "histo.png", dpi=150)

# 3. A single box plot for math, python, db -> box.png
fig, ax = plt.subplots(figsize=(6, 5))
scores[COURSES].plot.box(ax=ax)
ax.set_title("Box plot of scores")
ax.set_ylabel("score")
ax.grid(True, axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(DIR / "box.png", dpi=150)

plt.show()
