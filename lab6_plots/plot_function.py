# Lab 6a: Matplotlib - plot y = 2x + sin^2(x) + 3

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)
y = 2 * x + np.sin(x)**2 + 3

plt.figure(figsize=(8, 5))
plt.plot(x, y, color="steelblue", linewidth=2)
plt.grid(True, linestyle="--", alpha=0.7)
plt.title("hello, po!")
plt.xlabel("x")
plt.ylabel("y = 2x + sin²(x) + 3")
plt.tight_layout()
plt.savefig("po.pdf")
print("Saved plot to po.pdf")
plt.show()
