import plotly
import plotly.plotly as py
import pandas as pd

# setup Plotly credentials
plotly.tools.set_credentials_file(username='', api_key='')

# read data set into Pandas DataFrame
df = pd.read_csv('../data/data_analysis.tsv', sep='\t')

# convert cost of living to strings
for col in df.columns:
    df[col] = df[col].astype(str)

# color scaling for interactive map
scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

# html for interactive map
df['text'] = df['STATE'] + '<br>' +\
    'Salary '+df['SALARY'] + '<br>'+\
    'Tax '+df['TAX']+'%<br>'+\
    'Cost of Living '+df['COST OF LIVING']

# init map data
data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = df['CODE'],
        z = df['ADJUSTED INCOME'].astype(float),
        locationmode = 'USA-states',
        text = df['text'],
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "USD")
        ) ]

# header layout
layout = dict(
        title = 'Average Software Engineer Takehome Salary by State<br>(Adjusted for state COL)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )

# plot map into html file
fig = dict( data=data, layout=layout )
plotly.offline.plot( fig, filename='d3-cloropleth-map' )
