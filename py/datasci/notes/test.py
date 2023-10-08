import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# make sure you have .show() for every plot you want to display as output

x = np.linspace(0, 5, 11)
y = x ** 2

# plt.plot(x,y)

# plt.xlabel('X Label')
# plt.ylabel('Y label')
# plt.title('Title')

# plt.subplot(1,2,1)
# plt.plot(x,y, 'r')

# plt.subplot(1,2,2)
# plt.plot(y,x, 'b')



fig = plt.figure()

# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# axes.plot(x,y)

# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Set Title')



axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

axes1.plot(x,y)
axes1.set_title('LARGER PLOT')

axes2.plot(y,x)
axes2.set_title('SMALLER PLOT')

plt.show()



