import numpy as np
import matplotlib.pyplot as plt

arr_1 = np.random.randint(1,7,7000)
arr_2 = np.random.randint(1,7,7000)

arr_3 = arr_2 + arr_1

plt.hist(arr_3, bins = 11, density=True, stacked=True)
plt.show()
