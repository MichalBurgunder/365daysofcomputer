import matplotlib.pyplot as plt

plt.xlim(0, 10)
plt.ylim(0, 3)

plt.plot([1,2,3], [1,1,1], label='Line 1', color='red')
plt.plot([4,5], [1,2], label='Line 2', color='blue')
plt.show()
plt.clf()

plt.xlim(0, 10)
plt.ylim(0, 3)

plt.plot([2,3,4], [1,1,1], label='Line 1', color='red')
plt.plot([4,5], [1,2], label='Line 2', color='blue')
plt.show()
plt.clf()

plt.xlim(-1, 5)
plt.ylim(-1, 3)

plt.plot([x/100 for x in range(0, 100)], [(x/100)**2 for x in range(0, 100)], label='Line 1', color='red')
plt.plot([x/100 for x in range(99, 200)], [(-(x/100-2)**2+2) for x in range(99, 200)], label='Line 2', color='blue')
plt.show()
plt.clf()