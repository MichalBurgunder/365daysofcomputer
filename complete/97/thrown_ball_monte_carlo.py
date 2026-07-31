# THROWN BALL SIMULATION

import math
import matplotlib.pyplot as plt
import random

dt = 0.01
g = 9.81

for i in range(0, 50):
    x = 0
    y = 0
    t = 0
    angle_degrees = random.random()*90
    initial_velocity = random.random()*4 + 4

    angle_radians = math.radians(angle_degrees)
    dxdt = initial_velocity * math.cos(angle_radians)
    dydt = initial_velocity * math.sin(angle_radians)

    xs = []
    ys = []

    while 0 <= y:
        x += dxdt*dt
        y += dydt*dt - 0.5*g*dt**2
        xs.append(x)
        ys.append(y)

        dydt -= g * dt
        t += dt

    plt.plot(xs, ys)

plt.title("Thrown Ball Monte Carlo Simulation")
ax = plt.gca()
ax.set_xlim([0, 6])
ax.set_ylim([0, 4])
plt.xticks([0, 1, 2, 3, 4, 5, 6])
plt.yticks([0, 1, 2, 3, 4])
plt.xlabel("Horizontal Distance")
plt.ylabel("Vertical Distance")
plt.show()