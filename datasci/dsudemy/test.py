import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt

# make sure you have .show() for every plot you want to display as output

x = np.linspace(0,5, 11)
y = x ** 2
# z = x ** 2

fig  = plt.figure()

ax1 = fig.add_subplot(1,1,1)
ax1.plot(x,y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Bigger Plot')


ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2 ])

ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')



plt.show()


