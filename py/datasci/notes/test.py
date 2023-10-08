import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# make sure you have .show() for every plot you want to display as output

x = np.linspace(0,5, 11)

y = x ** 2

fig, axes = plt.subplots(1 , 2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('Second Plot')


plt.tight_layout()

plt.show()


