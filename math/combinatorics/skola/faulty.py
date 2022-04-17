import numpy as np

n = int(1e7)
m = 60
p = 0.05

result = np.sum(np.random.uniform(0, 1, [n, m]) > 1 - p, axis=1) <= 4
print(np.sum(result) / n)

print("sus", "sjkldfa", "kasjldf", sep="a")
