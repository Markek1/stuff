from matplotlib import pyplot as plt
import math

# this program shows the side lengths of a right triangle, and the derivative of a side length in the falling ladder calculus problem

constant = 5 # lenght of the hypotenuse
dt = 0.0001 # unit of time. More accurate results with a smaller dt
b_speed = -1 # per unit of time
a_values = [3]
b_values = [4]
t = [0]
d = []

while a_values[-1] < constant and b_values[-1] > 0:
    b_values.append(b_values[-1] + dt * b_speed)
    a_values.append(math.sqrt(constant ** 2 - b_values[-1] ** 2))
    t.append(t[-1] + dt)
    d.append((a_values[-1] - a_values[-2]) / dt)
d.append((a_values[-1] - a_values[-2]) / dt) # need to do this a second time so it has the same length as t. The more accurate alternative is creating d with the calculated derrivative at t=0

plt.plot(t, a_values, label='len of side a')
plt.plot(t, b_values, label="len of side b")
plt.plot(t, d, label="d of the len of side a")
plt.legend()
plt.show()

# print(a_values)
# print(b_values)
# print(t)