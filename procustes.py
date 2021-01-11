import numpy as np
from scipy.spatial import procrustes

a = np.array([[1, 3,4], [1, 2,2], [1, 1,6], [2, 1,5]], 'd')
b = np.array([[4, -2,3], [4, -4,7], [4, -6,5], [2, -6,1]], 'd')
mtx1, mtx2, disparity = procrustes(a, b)
round(disparity)
print(1)
