# import the relevant libraries: plotly express and pandas
import pandas as pd # To work with tabular data 
import plotly.express as px # To make maps from extracted place names 

# Load the tsv files required to make the data frame for the maps 
#Load the tsv file with the frequency data into Data Frame:

freq_df = pd.read_csv("regex_counts.tsv", sep="\t")

#load the gazetteer tsv file that contain coordinates for the map and load into data frame
gazetteer_path = "gazetteers/geonames_gaza_selection.tsv"
coordinates_df = pd.read_csv(gazetteer_path, sep="\t")

#To remove placenames without coordinates from the data frame:
coordinates_df = coordinates_df.dropna()

# print the dataframe:
print(freq_df)
print(coordinates_df)

#Rename asciiname in coordinates  dataframe with placenames in frequency dataframe to have a commmon name column after merging

coords_renamed = coordinates_df.rename(columns={'asciiname': 'placename'})


#Merge the two data frames to match place name with its coordinates, using the common column "asciname"
merged_df = pd.merge(coordinates_df, freq_df, on = "placename")

print(merged_df)



# change some settings to make the dataframe print nicer
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option("max_colwidth", 15)

#display on a map, with frequency defining the size of the markers:
fig = px.scatter_map(merged_df, lat ="latitude", lon="longitude",
                     hover_name = "placename", size= "frequency",color="frequency",
                     color_continuous_scale = px.colors.sequential.ylorRd,
                     animation_frame = "month")
fig.update_layout(map_style= "carto-darkmatter-nolabels")



# display it in the browser:
fig.show()
