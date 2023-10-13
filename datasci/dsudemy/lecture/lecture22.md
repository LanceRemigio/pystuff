# Matrix Plots


## Heat maps

### Using correlation function to turn data table into matrix form

We need to get the data into matrix form before we apply the heat map to it.

We can do either a **correlation table** or a **pivot table** to get our data into a matrix form.
Suppose we have the example data set.
````python
import seaborn as sns
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
tips.head() # checks out the first few rows of the data set
````

Then turning the dataset into a matrix form, we can do 
````python
tc = tips.corr()
sns.heatmap(tc)
````
- Colors in values based on a gradient scale. 
- Larger correlation of data is associated with a greater intensity of color.

We can specify a `color map` on the heat map data. We can do this by typing the following code:
````python
sns.heatmap(tc, annot = True, cmap = 'coolwarm')
````

### Turning data table into matrix form using pivot tables

Looking back to our flights table, we can use the `pivot_table` function to turn our data table into a matrix form.
````python
tc = flights.pivot_table(index = 'month', columns = 'year', values = 'passengers')
````
We can pass this variable into our `heatmap` function
````python
sns.heatmap(tc)
````
Sometimes heatmaps can be hard to read. We can solve this problem by passing in a `linewidth` argument as well as the `linecolor` argument. We can do this by typing the following code:
````python
sns.heatmap(tc, cmap = 'pick_color', linecolor = 'color', linewidth = 2)
````

## Cluster Maps

Clusters data in groups that are similar to each other.



