# Lecture 19

## Plot Appearance


````python
import matplotlib as plt 
import numpy as np

x = np.linspace(0,5,11) 


fig  = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y, color = 'orange', linewidth = 1, alpha = 0.5) # specify colors as strings or rgb hex codes 
# can also specify linewidth
````

We can specify a dashed line if we want to display a discrete graph
````python
ax.plot(x,y, color = 'purple', lw = 3, linestyle = '-' ) # specify the markers as strings
````



We can mark out each point on our graphs by specifying a string argument

There are a lot of options to customize marking on plots.
````python
ax.plot(marker = 'o', markersize = 20, markerfacecolor = 'yellow') 
````

## Settings a lower bound and upper bound on plots

We can set custom bounds on our plots

````python
ax.set_xlim([0,1])
ax.set_ylim([0,2])
````













