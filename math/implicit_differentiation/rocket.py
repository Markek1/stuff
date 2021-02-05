from matplotlib import pyplot as plt
import math
import numpy as np

A = 350
d_b = 15

b_sizes = []
c_sizes = []
d_c_sizes = []

n_of_steps = 1000
time_steps = np.linspace(0, 60, n_of_steps)

for step in time_steps:
    b = d_b * step
    b_sizes.append(b)
    c = math.sqrt(A ** 2 + b ** 2)
    c_sizes.append(c)
    d_c_sizes.append((b * d_b) / c)

d_b_sizes = np.full((n_of_steps), d_b)

plt.plot(time_steps, b_sizes, label='b length')
plt.plot(time_steps, c_sizes, label='c length')
plt.plot(time_steps, d_b_sizes, label='d of b')
plt.plot(time_steps, d_c_sizes, label='d of c')

plt.legend()
plt.show()
