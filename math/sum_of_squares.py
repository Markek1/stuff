import matplotlib.pyplot as plt

def gradual_sum_squares(N):
    sums = []
    cur_sum = 0
    for n in range(1, N + 1):
        cur_sum += n ** 2
        sums.append(cur_sum)

    return sums


def gradual_empty_size(N):
    sums = []
    cur_sum = 0
    for n in range(N):
        cur_sum += n * (2 * n + 1)
        sums.append(cur_sum)

    return sums


N = 100

sum_squares = gradual_sum_squares(N)
empty_sizes = gradual_empty_size(N)

i_format = len(str(N))
ss_format = len(str(max(sum_squares)))
es_format = len(str(max(empty_sizes)))

for i, (ss, es) in enumerate(zip(sum_squares, empty_sizes)):
    print(f'{i:{i_format}}, {ss:{ss_format}}, {es:{es_format}}')

plt.plot(range(N), sum_squares, color='red')
plt.plot(range(N), empty_sizes, color='blue')
plt.show()