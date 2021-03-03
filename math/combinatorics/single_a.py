from itertools import product

chars = ['a', 'b', 'c', 'd']
n = len(chars)
r = 4

def contains_one(_list, el):
    if _list.count(el) == 1:
        return True
    return False

total = 0
for x in product(chars, repeat=r):
    if contains_one(x, 'a'):
        total += 1

print(total / n ** r)
print((r * ((n - 1) / n) ** (r - 1)) / n)