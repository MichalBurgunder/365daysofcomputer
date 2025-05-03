import numpy as np
import matplotlib.pyplot as plt

number_of_waves = 15

x = np.linspace(0, number_of_waves*(2*np.pi), 1000)
y = np.sin(x)

x_sampled = np.linspace(0, number_of_waves*(2*np.pi), 40)
y_sampled = np.sin(x_sampled)

plt.plot(x, y, color='blue',label="Original Signal")
plt.plot(x, y, color='green',label='Reconstructed Signal')

plt.ylim(-5,5)
plt.scatter(x_sampled, y_sampled, color='red', label='Sampled points', zorder=5)
plt.title("Sample rate > 2t frequency of signal")
plt.xlabel("t")
plt.ylabel("sin(t)")
plt.legend()
plt.grid(True)

# Show plot
plt.show()

number_of_waves = 30

x = np.linspace(0, number_of_waves*(2*np.pi), 1000)
y = np.sin(x)

x_sampled = np.linspace(0, number_of_waves*(2*np.pi), 30)
y_sampled = np.sin(x_sampled)

y_best_fit = np.sin(x/30)
plt.plot(x, y, color='blue', label="Original Signal")
plt.plot(x, y_best_fit, color='green', label='Reconstructed Signal')

plt.ylim(-5,5)
plt.scatter(x_sampled, y_sampled, color='red', label='Sampled points', zorder=5)
plt.title("Sample rate < 2t frequency of signal")
plt.xlabel("t")
plt.ylabel("sin(t)")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
