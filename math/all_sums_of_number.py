def sums(n):
    for i in range(2 ** (n - 1) - 1):
        _sum = []
        tmp = 1
        for j in range(n - 1):
            if not i & (1 << j):
                _sum.append(tmp)
                tmp = 1
            else:
                tmp += 1
        _sum.append(tmp)
        print(_sum[::-1])


n = int(input('Input number: '))
sums(n)
