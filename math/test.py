import dis

def is_odd_and(n):
    return n & 1 == 1

def is_odd_mod(n):
    return n % 2 != 0

print(dis.dis(is_odd_and))

print(dis.dis(is_odd_mod))