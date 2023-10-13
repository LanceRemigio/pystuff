# Seaborn

## Concepts

- distplot
- jointplot
- paitplot
- rugplot
- kdeplot



To import seaborn we will have to type the following:

````python
import seaborn as sns
````


## Distplot




We can do a distribution plot for a univariate set of data (single column from data frame) by typing the following code:
````python
sns.distplot(dt['column']) # dt = data_table
````
If we pass in `kde = false`, then we only get a bar graph.



## Jointplot

If we want to compare two distributions (bivariate), then we will have to type the following code:
````python
sns.jointplot(x = 'column1', y = 'column2', data = data_frame)
````

We can specify how we want to visualize our data by passing in either one of **kind** parameters to compare with:
- "scatter"
- 'reg'
- 'kde'
- 'hex'

````python
sns.jointplot(x = 'column1', y = 'column2', data = data_frame)
````
