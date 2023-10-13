# Categorical Plots

## Barplot

Aggregates data based on chosen numerical data associated with categorical data.

We can do this by typing:

````python
import seaborn as sns
sns.barplot(x = 'category', y = 'numerical data', data = data_table)
````

Barplot averages (mean) numerical data based each categorical bin. We can pass in an estimator function using numpy to find the variance in the data. Suppose we did this by using the standard deviation function from numpy. Then we type the following code:
````python
import seaborn as sns
import numpy as np
sns.barplot(x = 'category', y = 'numerical', data = data_table, estimator = np.std)
````

## Countplot

This time the estimator counts the **number of occurences** of each categorical bin.

All we need to do is pass in the category and the data table. Hence, we have

````python
sns.countplot(x = 'category', data = data_table)
````

## Box plot

We can visualize data as boxplots. We can do this by passing in the following arguments in the `boxplot()` function:
````python
sns.boxplot(x = 'column1', y = 'column2', data = data_table) # columns refer to numerical data
````

We can do more analysis by passing in a `hue` argument that seperates each data based on a vategory. We can do this by typing the following:
````python

sns.boxplot(x = 'column1', y = 'column2', data = data_table, hue = 'some_category') # 
````

## Violin Plots

Give us more information of the distribution of the points in our data we are analyzing.

````python
sns.violinplot(x = 'column1', y = 'column2', data = data_table) # columns refer to numerical data
````


## Stripplot

Can't tell how many points are stacked on top of each other or density of the points.

````python

sns.boxplot(x = 'column1', y = 'column2', data = data_table, hue = 'some_category') # 
````

We can pass in `jitter = True ` to show the density of points for each categorical data.


## Swarmplot

Shows all the points but does not scale well to larger data sets.

In any case, we can plot data by typing the following:

````python

sns.swarmplot(x = 'column3', y = 'column2', data = data_table) 
````

## Factor plots

````python
sns.swarmplot(x = 'column3', y = 'column2', data = data_table, kind = 'what kind of plot') # can be bar, violinplot, etc. 
````


