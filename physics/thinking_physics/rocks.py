import numpy as np


dt = 0.01

pos = np.array([[0.0, 1000.0], [0.0, 1005.0]])
v = np.zeros(2, dtype=np.float64)
print(v.dtype)
a = -9.8

t = 0
while t < 10:
    v += a
    pos += v

    print(pos[0, 1] - pos[1, 1])

    t += dt
