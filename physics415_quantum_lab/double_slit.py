import numpy as np
import matplotlib.pyplot as plt

# points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])
# # get x and y vectors
# x = points[:,0]
# y = points[:,1]

# voltage = np.zeros(31)
#
# for i in np.arange(31):
#     voltage[i] = 300 + 10*i
#
# print voltage

voltage = np.arange(300, 660, 10)

print float(voltage[0])

voltage.astype(float)

max_rate = np.array([0, 0, 0, ])



# # calculate polynomial
# z = np.polyfit(x, y, 3)
# f = np.poly1d(z)
#
# # calculate new x's and y's
# x_new = np.linspace(x[0], x[-1], 50)
# y_new = f(x_new)
#
# plt.plot(x,y,'o', x_new, y_new)
# plt.xlim([x[0]-1, x[-1] + 1 ])
# plt.show()