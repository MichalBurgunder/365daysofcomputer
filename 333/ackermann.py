import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def A(x, y):
    if x == 0:
        return y + 1
    if y == 0:
        return A(x-1,1)
    return A(x-1, A(x,y-1))

# for x in range(0,5):
#     for y in range(0,3):
#         print(A(x,y))

# print(A(4,0))

xs = np.array([0,1,2,3,4,5])
ys_exp = np.array([10**i for i in xs])
ys_ackermann = np.array([2,3,5,13,65533,1000000000000000]) # it's not 100000, but visually irrelevant

smooth_xs = np.linspace(xs.min(), xs.max(), 100)

exp_spline = make_interp_spline(xs, ys_exp, k=1)
ackermann_spline = make_interp_spline(xs, ys_ackermann, k=1)

# Returns evenly spaced numbers
# over a specified interval.

ys_exp = exp_spline(smooth_xs)
ys_ackermann = ackermann_spline(smooth_xs)

# print(ys_ackermann)

plt.plot(smooth_xs, ys_exp, label="Exponential 10^x")
plt.plot(smooth_xs, ys_ackermann, label="Ackermann A(x,1)")
# plt.plot(xs, ys_exp)
# plt.plot(xs, ys_ackermann)
plt.ylim(0, 100000)
plt.xlim(0, 5)
plt.legend()
# plt.hist(speeds, bins=num_bins, weights=probability_densities, color=(97/256, 0/256, 198/256), edgecolor='black')
plt.title("Ackermann vs Exponential Complexity")
plt.xlabel("x")
plt.ylabel("y")
plt.show()