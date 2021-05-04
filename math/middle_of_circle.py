from math import sqrt

p = [9, 9]
q = [2, 16]
r = 17

d = sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

x3 = (p[0] + q[0]) / 2
y3 = (p[1] + q[1]) / 2

base = sqrt(r ** 2 - (d / 2) ** 2)
base_x = base * (q[1] - p[1]) / d
base_y = base * (p[0] - q[0]) / d

print(x3 + base_x, y3 + base_y)
print(x3 - base_x, y3 - base_y)
