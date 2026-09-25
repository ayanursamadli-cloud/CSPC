"""
PW2 Lab A -- Bonus: 2D tracked trajectory.

trajectory.csv has time,x,y: a noisy tracked position in a plane.
We differentiate x and y separately to get velocity components,
then compute the speed = sqrt(vx^2 + vy^2).

Run:
python trajectory_analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Read trajectory.csv into t, x, y
t, x, y = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1, unpack=True)

# Differentiate x and y separately to get velocity components
vx = np.gradient(x, t)
vy = np.gradient(y, t)

# Speed = sqrt(vx^2 + vy^2)
speed = np.sqrt(vx**2 + vy**2)

# Plot 1: the path (x vs y)
fig1, ax1 = plt.subplots(figsize=(6, 6))
ax1.plot(x, y, color="tab:purple")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.set_title("Tracked path")
ax1.set_aspect("equal")
plt.tight_layout()
plt.savefig("trajectory_path.png", dpi=150)

# Plot 2: speed over time
fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.plot(t, speed, color="tab:red")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Speed (m/s)")
ax2.set_title("Speed vs time")
plt.tight_layout()
plt.savefig("trajectory_speed.png", dpi=150)

plt.show()
