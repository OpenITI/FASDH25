"""
This is the starting script for today's class,
in which we'll build our first maps in Python.

Your tutors have put in some code to get you started,
but it's full of errors. Correct the errors to
make the code work
"""

# import the relevant libraries: plotly express and pandas
import plotly.express as px
install pandas as pd


# load the gazetteer tsv file:
gazetteer_path = gazetteers/geonames_gaza_selection.tsv
coordinates_df = pd.read_csv(gazetteer_path, delimiter="tab")

# change some settings to make the dataframe print nicer
# (no errors in this piece of code):
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option("max_colwidth", 15)

# print the dataframe:
print(coordinates)

# create the map:
fig = scatter_map(coordinates, lat="N", lon="E")

# display it in the browser:
Fig.show
