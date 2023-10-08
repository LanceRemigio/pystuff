## Mathplotlib Concepts 

## Basics

### Functional Method of Plotting graphs

To import the module into a python file, you will need to type the following:
````python
import matplotlib.pyplot as plt
````




Suppose we want to graph a quadratic function $x^2$. In order to plot this function, we will need to specify the number of points 

````python
x = np.linspace(0, 5, 11)
y = x ** 2

````

The most basic way to plot this graph is to type the following:
````python
plt.plot(x,y)
plt.show() # Need this if you're in a basic ide/text editor
````

We can label our axes by typing the following:

````python
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Title')
````
We should display the following graph


## Object Oriented Method for implementing plots




````python
fig = plt.figure() #acts as our blank canvas

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # set axes of graph [left, bottom, width, height]
# range from 0 <= height <= 1
axes.plot(x,y)

axes.set_xlabel('X Label') # sets x-axis label
axes.set_ylabel('Y Label') # sets y-axis label
axes.set_title('Set Title') # sets title

plt.show()
````

## Plots within plots

We can create plots within plots on the same figure typing the following:

````python
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

````
Plotting and adding titles to our smaller plot is just a matter of doing the following:
````python
axes1.plot(x,y) # this plots the large graph
axes1.set_title('LARGER PLOT') 

axes2.plot(y,x) # this plots the smaller plot within the larger one
axes2.set_title('SMALLER PLOT')
````





