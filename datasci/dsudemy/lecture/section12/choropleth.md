# Choropleth Lecture

First, we need to do our usual imports 

````python
import numpy as np
import pandas as pd
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
%matplotlib inline
cf.go_offline() # this is only if you are using notebooks
import plotly.graph_objs as geo
````


We create the data using dictionaries. This can be done by typing the following code:
````python
data = dict(
            type = 'chropleth',
            locations = ['AZ', 'CA', 'NY'], # specify states
            locationmode = 'USA-states', 
            colorscale = 'Portland', 
            text = ['text1', 'text2', 'text3'], # the text that pops up when you hover cursor over locations specified in locations
            z = [1.0, 2.0, 3.0], # indicates value over each state
            colorbar = {'title': 'Colorbar Title Goes Here'} # title of colorbar
)
````

In addition to the code above, we also need to specify the scope of the chloropeth graph:
````python
layout = dict(geo={'scope': 'usa'})
go.Figure(data = [data], layout = layout)
````

## Basic Idea:

- We're going to have two objects, the `data` and `layout` objects.
- Both the `data` object and `layout` object is created out of a dictionary either by using `dict()` or the usual method for creating dictionaries (the former is recommended).
- In the `data` object, we specify the type, locations, locationsmode, colorscale, text, z-values (usually created out of values from a column), and colorbar. Basically, the `data` object is tasked with creating the choropleth map itself.
- On the other hand, the `layout` object is tasked with creating the basic labelling of features of the map.
- We pass these in to our the `Figure()` method as two arguments:
    ````python
    choromap = go.Figure(data = [data], layout = layout)
    ````
- Then pass in `choromap` into the `iplot()` function:
    ````python
    iplot(choromap)
    ````


## Example

Suppose we wanted to create a Choropleth map using the 2011 US agriculture exports data. 

````python
df = pd.read_csv('2011_US_AGRI_Exports')
df.head()
````

which should return the following data frame:

````
  code        state category  ...  wheat   cotton                                               
text
0   AL      Alabama    state  ...   70.0   317.61  Alabama<br>Beef 34.4 Dairy 4.06<br>Fruits 25.
1...
1   AK       Alaska    state  ...    0.0     0.00  Alaska<br>Beef 0.2 Dairy 0.19<br>Fruits 0.0 V
e...
2   AZ      Arizona    state  ...   48.7   423.95  Arizona<br>Beef 71.3 Dairy 105.48<br>Fruits 6
0...
3   AR     Arkansas    state  ...  114.5   665.44  Arkansas<br>Beef 53.2 Dairy 3.53<br>Fruits 6.
8...
4   CA   California    state  ...  249.3  1064.95   California<br>Beef 228.7 Dairy 929.95<br>Fru
i...

[5 rows x 18 columns]
````



We can make our data dictionary by typing the following:
````python
data = dict(type = 'choropleth',
            colorscale = 'YIOrRd',
            locations = df['code'],
    )

````



