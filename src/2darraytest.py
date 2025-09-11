import numpy as np

x, y = np.meshgrid([1, 2, 3], [4, 5, 6])
z = (zip(x.ravel(), y.ravel()))
print(z)