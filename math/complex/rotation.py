from math import sin, cos, pi

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

TURN_RATE = pi / 30
AXIS_SIZE = 1.5
NUM_OF_POINTS = 10
INTERVAL = 20

nums = np.random.uniform(-1, 1, (NUM_OF_POINTS,)) + np.random.uniform(-1, 1, (NUM_OF_POINTS,)) * 1j

fig, ax = plt.subplots()
plt.gca().set_aspect('equal', adjustable='box')
ln, = plt.plot([], [], 'b')

def init():
    ax.set_xlim(-AXIS_SIZE, AXIS_SIZE)
    ax.set_ylim(-AXIS_SIZE, AXIS_SIZE)
    return ln,

def update(i):
    global nums
    nums *= complex(cos(TURN_RATE), sin(TURN_RATE))
    ln.set_data(nums.real, nums.imag)
    return ln,

ani = animation.FuncAnimation(fig, update, init_func=init, blit=True, interval=INTERVAL)
plt.show()
