import numpy as np
from numpy import dot, arccos
from numpy.linalg import norm


def vector_angle(a, b):
    return arccos(abs(dot(a, b) / (norm(a) * norm(b))))


v = np.array([1, 2, 3])
u = np.array([4, 5, 6])

print(vector_angle(v, u))
