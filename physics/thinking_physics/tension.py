import numpy as np
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

F = 10
angle = pi / 2

origin = np.array([0, 0])

fig, ax = plt.subplots(figsize=(8, 8))
line, = ax.plot(0, 0)
plt.subplots_adjust(left=0.1, bottom=0.25)


def calculate(F, angle):
    a_len = F / (2 * cos(angle / 2))
    compl_ang = (pi - angle) / 2
    a_coors = a_len * np.array([cos(compl_ang), sin(compl_ang)])
    a_vec1 = a_coors
    a_vec2 = a_coors * (-1, 1)



    black_vecs = np.array((np.array([0, F]), a_vec1, a_vec2))
    _kwargs = {'angles': 'xy',
               'scale_units': 'xy',
               'scale': 1}
    ax.quiver([0, 0, 0], [0, 0, 0], black_vecs[:, 0], black_vecs[:, 1], **_kwargs, color='black')
    ax.quiver(a_vec1[0], a_vec1[1], a_vec2[0], a_vec2[1], **_kwargs, color='#dddddd')
    ax.quiver(a_vec2[0], a_vec2[1], a_vec1[0], a_vec1[1], **_kwargs, color='#dddddd')

    return a_len

def update(*args):
    F = s_F.val
    angle = s_angle.val

    ax.cla()
    a_len = calculate(F, angle)
    ax.set_ylim([0, 50])
    ax.set_xlim([-100, 100])
    ax.text(-97, 47, f'Tension = {a_len}')
    fig.canvas.draw_idle()


ax_F = plt.axes([0.15, 0.10, 0.65, 0.03])
ax_angle = plt.axes([0.15, 0.05, 0.65, 0.03])

s_F = Slider(ax_F, 'Vertical Force', 0.1, 50, valinit=F)
s_angle = Slider(ax_angle, 'Angle', 0, pi, valinit=angle)

s_F.on_changed(update)
s_angle.on_changed(update)

update()
plt.show()