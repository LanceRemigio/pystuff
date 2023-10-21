# Plotly and Cufflinks

## Disclaimer: Things to watch out for


1. Possible Import Error 1: You need to install a new package. In your command line type and run
````
pip install chart-studio
````

Then in jupyter make sure you import it by running the code:
````python
import chart_studio.plotly as py
````


2.Possible Colorscale Error 2: In the "Real Data US Map Choropleth", when you are creating the data dictionary, make sure the colorscale line is = 'ylorbr', not 'YIOrbr'... so like this:

colorscale='ylorbr'


3.Possible projection Error 3: In the "World Map Choropleth", when you are creating the layout, ensure that your projection line is = {'type':'mercator'} not Mercator with a capital...so like this:

projection={'type':'mercator'}


````python
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32,43,50]})
````

## Scatter Plots

````python
df.iplot(kind = 'scatter', x = 'A', y= 'B', mode = 'markers', size = 5.0) # interactive scatter plot 
````

## Bar Plots

````python
df2.iplot(kind = 'bar', x = 'Category', y = 'Values') # This plots an interactive bar plot
````

If we take our original bar plot, we get back a plot that may not be so easy to work with; that is, plotly will create a bar for each row in the data frame. For this, we will have to apply an aggregate function like `count()` to yield more useful information about our dataframe.

## 3D Surface Plots

Suppose we make the following dataframe with three columns x,y, and z:
````python
df3 = pd.DataFrame({'x': [1,2,3,4,5], 'y': [10,20,30,20,10], 'z': [500,400,300,200,100]})
df3.iplot(kind = "surface")
````


## Histograms 

````python
df['A'].iplot(kind = 'hist', bins = 50)
````

If we don't specify the column then we will just get a bunch of histograms overlapping each other.

````python
df.iplot(kind = 'hist')
````

