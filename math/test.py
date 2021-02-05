import random
from math import factorial as f

w = 20
a = 150
g = 20

result = (f(g) * f(a - w)) / (f(a) * f(g - w))
print(result)