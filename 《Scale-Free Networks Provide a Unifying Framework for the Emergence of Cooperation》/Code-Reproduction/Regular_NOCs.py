import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
plt.ylabel("frequnency of cooperators")

ax1 = plt.subplot(2, 2, 1)
plt.title("Prisoner’s Dilemma")

xpoints = []
ypoints = []
# for _k in [4, 16, 32, 64]:
for _b in np.arange(1, 1.2, 0.025):
    xpoints.append(_b)
    ypoints.append(_b)
plt.plot(xpoints, ypoints, ms = 4)



ax2 = plt.subplot(2, 2, 2)
plt.title("Snowdrift Game")

ax3 = plt.subplot(2, 2, 3)
plt.xlabel("b")

ax4 = plt.subplot(2, 2, 4)
plt.xlabel("r")


plt.show()