# Matplotlib Part 2



## subplots()

The `plt.subplots()` object acts as an automatic axis manager. The code below represents the typical way `subplots()` can be used to make graphs: 
````python
# Similar to plt.figure() but uses tuple unpacking to grab fig and axes
fig, axes = plt.subplots()

# the axes object adds labels to our plot
axes.plot(x,y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
````

We can specify how many rows and colums we want when creating the `subplots()` object. 
````python
fig, axes = plt.subplots(nrows = 1, ncols = 2) # gives us one row containing two plots.
````

We can use a for loop to iterate through the `axes` array object and the plots specified above:
````python
for ax in axes:
    ax.plot(x,y, 'b')
    ax.set_xlabel('x')
    ax.set_title('title')

plt.show()
````
Sometimes we may have some overlapping occur in displaying our subplots. We can fix this by adding `plt.tight_layout()` at the bottom of our code. This automatically adjust the position of the axes such that no overlapping content occurs.


## Figure Size and DPI

Matplotlib allows us to adjust the size, aspect ratio, and dpi using the parameters:
     - `figsize` is a tuple of the width and height of the figure in inches  
     - `dpi` si the dots-per-inch (pixel per inch)



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

````python
fig.savefig("somefile.png", dpi = 200) # saves plot as a png file
````



## Legend


Suppose we had to functions graphed on the same plot and needed a way to tell which function is which:
````python
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x, x **2)
ax.plot(x, x ** 3)
plt.show()
````
Without any further information, we wouldn't know which function is which.

We can do this using the `legend()` function. We need to specify a label on our plots; that is,
````python
ax.plot(x, x ** 2, label = 'x^2') # add labels to your plots
ax.plot(x, x ** 3, label = 'x^3')
ax.legend()
plt.show()
````
We can move the legend via location codes which range from 0 to 10; in other words, we have
````python
# Lots of options....

ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner

# .. many more options are available

# Most common to choose
ax.legend(loc=0) # let matplotlib decide the optimal location
fig
````









