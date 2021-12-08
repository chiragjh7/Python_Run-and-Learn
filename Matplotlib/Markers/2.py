# This parameter is also called fmt, and is written with this syntax:
# marker|line|color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')
plt.show()