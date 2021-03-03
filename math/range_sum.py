n1, n2 = [int(x) for x in input().split()]

def range_sum(n1, n2):
    if n1 > n2:
        n1, n2 = n2, n1

    if (n2 - n1) % 2 != 0:
        return (n1 + n2) * (n2 - n1 + 1) // 2
    else:
        return (n1 + n2 + 1) * (n2 - n1) // 2 + n1

print(range_sum(n1, n2))