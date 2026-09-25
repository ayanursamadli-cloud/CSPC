"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Run:
python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
t, y = np.loadtxt("freefall.csv", delimiter=",", skiprows=1, unpack=True)

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration:      {a.mean():.4f} m/s^2")
print(f"Std dev of acceleration: {a.std():.4f} m/s^2")

# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_recovered = cumulative_trapezoid(a, t, initial=0) + v[0]
y_recovered = cumulative_trapezoid(v_recovered, t, initial=0) + y[0]

max_diff = np.max(np.abs(y_recovered - y))
print(f"Max |y_recovered - y|:   {max_diff:.4f} m")

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)

axes[0].plot(t, y, color="tab:blue")
axes[0].set_ylabel("Position y (m)")
axes[0].set_title("Free-fall tracking: position, velocity, acceleration")

axes[1].plot(t, v, color="tab:orange")
axes[1].set_ylabel("Velocity v (m/s)")

axes[2].plot(t, a, color="tab:green")
axes[2].axhline(-9.81, color="red", linestyle="--", label="-9.81 m/s$^2$ (true g)")
axes[2].set_ylabel("Acceleration a (m/s^2)")
axes[2].set_xlabel("Time (s)")
axes[2].legend()

plt.tight_layout()
plt.savefig("motion.png", dpi=150)
plt.show()