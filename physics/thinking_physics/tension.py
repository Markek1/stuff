from matplotlib.widgets import Slider
from numba import njit
from numpy import sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np

F = 10
angle = pi / 2

origin = np.array([0, 0])

fig, ax = plt.subplots(figsize=(8, 8))

(line,) = ax.plot(0, 0)
plt.subplots_adjust(left=0.1, bottom=0.25)

_kwargs = {"angles": "xy", "scale_units": "xy", "scale": 1}


@njit
def calculate(F, angle):
    a_len = F / (2 * cos(angle / 2))
    compl_ang = (pi - angle) / 2
    a_coors = a_len * np.array([cos(compl_ang), sin(compl_ang)])
    a_vec2 = a_coors * np.array([-1.0, 1.0])

    return a_len, a_coors, a_vec2


def draw_vects(F, angle):
    a_len, a_coors, a_vec2 = calculate(F, angle)

    ax.quiver(
        [0, 0, 0],
        [0, 0, 0],
        [0, a_coors[0], a_vec2[0]],
        [F, a_coors[1], a_vec2[1]],
        **_kwargs,
        color="black",
    )
    ax.quiver(a_coors[0], a_coors[1], a_vec2[0], a_vec2[1], **_kwargs, color="#dddddd")
    ax.quiver(a_vec2[0], a_vec2[1], a_coors[0], a_coors[1], **_kwargs, color="#dddddd")

    return a_len


def update(*args):
    if s_F.val is None or s_angle.val is None:
        return

    ax.cla()
    a_len = draw_vects(s_F.val, s_angle.val)
    ax.text(-97, 47, f"Tension = {a_len}")
    ax.set_ylim([0, 50])

    ax.set_xlim([-100, 100])


ax_F = plt.axes([0.15, 0.10, 0.65, 0.03])
ax_angle = plt.axes([0.15, 0.05, 0.65, 0.03])

s_F = Slider(ax_F, "Vertical Force", 0.1, 50, valinit=F)
s_angle = Slider(ax_angle, "Angle", 0, pi, valinit=angle)

s_F.on_changed(update)
s_angle.on_changed(update)

update()
plt.show()
