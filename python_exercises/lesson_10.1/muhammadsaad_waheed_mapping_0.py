"""
This is the starting script for today's class,
in which we'll build our first maps in Python.
"""

# import the relevant libraries: plotly express and pandas
import pandas as pd
import plotly.express as px

# load the gazetteer tsv file:
gazetteer_path = "gazetteers/geonames_gaza_selection.tsv"
coordinates = pd.read_csv(gazetteer_path, sep="\t")


# change some settings to make the dataframe print nicer
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option("max_colwidth", 15)

# print the dataframe:
print(coordinates)

# create the map:
fig= px.scatter_map(coordinates, lat="latitude", lon="longitude")

# display it in the browser:
fig.show()
