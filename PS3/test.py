import numpy as np

a = np.array([[1, 0], [0, 1]])
b = np.array([[1, 2, 3], [3, 4, 5]])
c = np.array([[1, 2, 1]])
print(b.shape)
d = np.dot(a,b)
for x in d:
    for j in range(0, d.shape[1]):
        x[j] += c[0][j]
print(d)
print(np.mean(d, axis=0))
