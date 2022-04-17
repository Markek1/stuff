from matplotlib import pyplot as plt
import numpy as np

plt.style.use('seaborn')

plt.plot(np.arange(0, 100), np.random.normal(0, 1, 100))
plt.show()
