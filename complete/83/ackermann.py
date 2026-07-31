# ACKERMANN FUNCTION VISUALIZATION IN PYTHON

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# the ackermann function.
def ackermann(x, y):
    if x == 0:
        return y + 1
    if y == 0:
        return ackermann(x-1,1)
    return ackermann(x-1, ackermann(x,y-1))

# to keep things simple, we do not actually compute the ackermann function, as we would need to manually set a new recurison limit. To see what I mean, try to execute the code below.
# print(ackermann(4,2))
# exit()

xs = np.array([0,1,2,3,4,5])
ys_exp = np.array([10**i for i in xs])

# the last value below is not the result of the ackermann function, but this is 
# visually irrelevant
ys_ackermann = np.array([2,3,5,13,65533,1000000000000000]) 

smooth_xs = np.linspace(xs.min(), xs.max(), 100)

exp_spline = make_interp_spline(xs, ys_exp, k=1)
ackermann_spline = make_interp_spline(xs, ys_ackermann, k=1)

ys_exp = exp_spline(smooth_xs)
ys_ackermann = ackermann_spline(smooth_xs)

plt.plot(smooth_xs, ys_exp, label="Exponential 10^x")
plt.plot(smooth_xs, ys_ackermann, label="Ackermann A(x,1)")
plt.ylim(0, 100000)
plt.xlim(0, 5)
plt.legend()
plt.title("Ackermann vs Exponential Complexity")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
