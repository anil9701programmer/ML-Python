import matplotlib.pyplot as plt
import numpy as np

# x_1 = np.linspace(1,10,50)
# y_1 = np.sin(x_1)
#
# fig = plt.figure(figsize=(6,4))
# axes = fig.add_axes([0,0,1,1])
#
# axes.plot(x_1,y_1,color="navy", alpha=.75,lw=2,ls='-.', marker='o', markersize=7, markerfacecolor='y', markeredgecolor='g', markeredgewidth=4)
# axes.set_xlim(0,4)
# axes.set_ylim(1,0)
# axes.plot(x_1,y_1,color="navy", alpha=.75,lw=2,ls='-.', marker='o', markersize=7, markerfacecolor='y', markeredgecolor='g', markeredgewidth=4)
# axes.grid(True)
# axes.set_facecolor('cyan')
# plt.show()

fig1 = plt.figure(figsize=(8, 4), dpi=100)
axes = fig1.add_axes([0.0, 0.0, 1, 1])
axes.set_title("Sample label")
axes.set_xlabel("days")
axes.set_ylabel("years")
plt.show()
