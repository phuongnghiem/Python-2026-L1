# Lab 6b: Pandas + Matplotlib plots

import pandas as pd
import matplotlib.pyplot as plt

scores = pd.read_csv("../data/scores.csv")

# 1. Scattered plot of math, python, db
plt.figure(figsize=(8, 6))
plt.scatter(scores.index, scores["math"], label="Math", alpha=0.7, s=80)
plt.scatter(scores.index, scores["python"], label="Python", alpha=0.7, s=80)
plt.scatter(scores.index, scores["db"], label="DB", alpha=0.7, s=80)
plt.xlabel("Student index")
plt.ylabel("Score")
plt.title("Student Scores - Scatter Plot")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("scattered.png", dpi=150)
print("Saved scattered.png")
plt.close()

# 2. Histogram of each course on subplots
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].hist(scores["math"], bins=5, color="skyblue", edgecolor="black")
axes[0].set_title("Math")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Frequency")

axes[1].hist(scores["python"], bins=5, color="lightgreen", edgecolor="black")
axes[1].set_title("Python")
axes[1].set_xlabel("Score")

axes[2].hist(scores["db"], bins=5, color="salmon", edgecolor="black")
axes[2].set_title("DB")
axes[2].set_xlabel("Score")

plt.suptitle("Histograms of Course Marks")
plt.tight_layout()
plt.savefig("histo.png", dpi=150)
print("Saved histo.png")
plt.close()

# 3. Box plot for math, python, db
plt.figure(figsize=(7, 5))
scores[["math", "python", "db"]].boxplot()
plt.title("Box Plot of Course Marks")
plt.ylabel("Score")
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("box.png", dpi=150)
print("Saved box.png")
plt.close()

print("All plots generated successfully.")
