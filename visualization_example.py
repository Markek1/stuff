import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(0, 100)
line, = ax.plot(0, 0)

def animate(i):
    x_data.append(i * 10)
    y_data.append(i)

    line.set_data(x_data, y_data)

    return line,

ani = FuncAnimation(fig, func=animate, frames=np.linspace(0, 10, 900), blit=True, interval=1)

plt.show()