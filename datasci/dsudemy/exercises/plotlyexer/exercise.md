# Choropleth Maps Exercises


## Plotly Imports 

````python
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
    ````

1. Import pandas and read the csv file: 2014_World_Power_Consumption.

````python
import pandas as pd
df1 = pd.read_csv('2014_World_Power_Consumption')
````

2. Check the head of the DataFrame.

````python
print(
    df1.head()
)
````


3. Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary.

````python
data = dict(
    type = 'choropleth',    
    location = df1['Country'],
    locationmode = 'country names',
    z = df1['Power Consumption KWH'],
    title = df1['Country'],
    text = df1['Text'],
    colorbar = {'title': 'Power Consumption KMH'}
)

layout = dict(
    title = '2014 World Power Consumption',
    geo = dict(
        showframe = False,
        projection = {'type': 'Mercator'}
    )
)

choromap = go.Figure(data = [data], layout = layout)
iplot(choromap, validate = False)

````

## USA Choropleth


1. Import the 2012_Election_Data csv file using pandas.

````python
df2 = pd.read_csv('2012_Election_Data') # import the data
print(
    df2.head() # checks the head of the data frame
)
````

2. Now create a plot that displays the **Voting-Age Population (VAP) per state**. 

````python
data = dict(
    type = 'choropleth',
    locations = df2['State Abv'],
    locationmode = 'USA-states',
    z = df2['Voting-Age Population (VAP)'],
    text = df['State'],
    colorbar = {'title': 'Voting-Age Population (VAP)'}
)

layout = dict(
    title = '2012 Election: Voting Age Population per State',
    geo = dict(
        scope = 'usa',
        showlakes = True,
        lakecolor = 'rgb(85,173,240)'
    )
)

choromap = go.Figure(data = [data], layout = layout)
iplot(choromap, validate = False)



````


