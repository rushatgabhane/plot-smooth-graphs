import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

# x axis values
X = np.array([30, 35, 45, 50, 55, 60])
# y axis values
Y = np.array([26, 25, 24, 25, 26, 27])

# Greater the smooth factor, smoother the curve and vice-versa
smooth_factor = 250
x = np.linspace(X.min(), X.max(), smooth_factor)

# Smmooothens the curve using spline
smooth = spline(X, Y, x)
plt.plot(x, smooth)
plt.plot(X, Y, '.')
plt.tight_layout()
plt.show()
