# Marker Size
# ms keyword
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = "o", ms = 20)
plt.show()