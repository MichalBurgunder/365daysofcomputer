# CURVE VISUALIZATION
import numpy as np
import matplotlib.pyplot as plt

# we create a rather simple paramatric curve with two trigonometric functions.

t = np.linspace(0, 9, 1000)  # 1000 points from 0 to 2π

x = t*1.5*np.cos(2*t)
y = t**1.2*np.sin(t)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Circle (Parametric)', color=(97/256, 0/256, 198/256), linewidth=4)
plt.title('Parametric Curve Example')

plt.show()