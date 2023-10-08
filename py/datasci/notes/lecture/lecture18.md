# Matplotlib Part 2

The  `axes` of a subplot  will give us an array object which means we can iterate through with a for loop.

When using `.subplots()`, the spefication of axes is automatically done for you unlike  `add_axes()` function (both have its upsides and downsides). 


## Figure Size and DPI

We can plot figures in two ways:

The first way deals with manually specifying the axes:
````python
x = np.linspace(0,5,11) # set up
y = x ** 2 

fig = plt.figure((3,2)) # Tuple represents the size of figure

ax = fig.add_axes([0,0,1,1]) # Specifying the axes

ax.plot(x,y)
````
The second way uses the OOP method:

````python
fig, axes = plt.subplots(2, 1 , (8,2)) # first two arguments specify the number of rows and columns respectively

axes[0].plot(x,y)

axes[1].plot(y,x)

plt.tight_layout()

````

## Saving Figures

We can use the `savefig()` method. Can be saved as either `.png`, `.pfg` file. We can also specify the quality of the figure by passing a dpi argument.


## Legend


Suppose we had to functions graphed on the same plot and needed a way to tell which function is which:
````python
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, x **2)
ax.plot(x, x ** 3)
plt.show()
````










