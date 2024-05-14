import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bms_data = pd.read_csv("bms.csv")
bms_data = bms_data.sort_values(by="Age")

np_arr = bms_data.values
x_1 = np_arr[:, 0]
y_1 = np_arr[:, 1]
z_1 = np_arr[:, 2]

# creating a figure object and consecutive graph
#
# fig = plt.figure()
# axes = fig.add_axes([0, 0, 1, 1])

plt.title("Body Mass Index")
# plt.plot(x_1,y_1,'--')
plt.xlabel("Age")
plt.ylabel("Height")

# plt.show()


# x = [1,2,3,4,5,6,7,8,9]

# y = [i**2 for i in x]
# print(x)
# print(y)

x = plt.plot(x_1,y_1)
# plt.title("Title")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
y = plt.plot(x_1,z_1)

plt.show()