import matplotlib.pyplot as plt
import math
import numpy as np

# sin waves
plt.xlim(-1, 15)
plt.ylim(-2, 2)

xs = np.linspace(0, 150, 1500)

plt.plot(xs, np.sin(xs), label='Line 1', color='red')
plt.plot(xs, np.sin(xs*1.05), label='Line 1', color='purple')
plt.plot(xs, np.sin(xs*1.1), label='Line 1', color='blue')
plt.plot(xs, np.sin(xs*1.15), label='Line 1', color='green')
plt.plot(xs, np.sin(xs*1.2), label='Line 1', color='orange')

plt.show()
plt.clf()

# parabolas 
plt.xlim(-15, 15)
plt.ylim(-2, 100)

xs = np.linspace(-150, 150, 1500)

plt.plot(xs, xs**2*0.5, label='Line 1', color='red')
plt.plot(xs, xs**2*1, label='Line 1', color='purple')
plt.plot(xs, xs**2*1.4, label='Line 1', color='blue')
plt.plot(xs, xs**2*2, label='Line 1', color='green')
plt.plot(xs, xs**2*3, label='Line 1', color='orange')

plt.show()
plt.clf()

# sin waves with polar coordinates
plt.subplot(projection='polar')

theta = np.linspace(0, 4*np.pi, 400)
r_flower_1 = 1*np.sin(6*theta)+4
r_flower_2 = 2*np.sin(7*theta)+6
r_flower_3 = 3*np.sin(8*theta)+8
r_flower_4 = 4*np.sin(9*theta)+10
# r_spiral = theta

# plt.plot(theta, r_spiral, color='red')
plt.plot(theta, r_flower_1, color='purple')
plt.plot(theta, r_flower_2, color='blue')
plt.plot(theta, r_flower_3, color='green')
plt.plot(theta, r_flower_4, color='red')

plt.grid(False)
plt.rgrids([])
plt.thetagrids([])

plt.show()