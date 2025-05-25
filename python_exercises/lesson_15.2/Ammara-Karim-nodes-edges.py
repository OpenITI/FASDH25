#importing required libraries
import pandas as pd
import plotly.express as px

#loading the data frame
df=pd.read_csv("data/tfidf-2024.csv")

#printing the first few rows to understand the structure
print(df.head())

#reaming the columns
edges_df = df.rename(columns={"filename-1": "Source",
                              "filrname-2": "Target",
                              "Similarity": "Weight"})

# Creating the edges list
edges = df[['filename-1', 'filename-2', 'similarity']]
edges.columns = ['Source', 'Target', 'Weight']

# Creatig the nodes list
source_nodes = df[['filename-1', 'title-1', 'month-1']]
source_nodes.columns = ['Id', 'Label', 'month']

target_nodes = df[['filename-2', 'title-2', 'month-2']]
target_nodes.columns = ['Id', 'Label', 'month']

# Combine and remove duplicate nodes
nodes = pd.concat([source_nodes, target_nodes]).drop_duplicates(subset='Id')

# writing the ouput to CSV
edges.to_csv('outputs/Ammara-Karim-edges.csv', encoding='utf-8-sig', index=False)
nodes.to_csv('outputs/Ammara-Karim-nodes.csv', encoding='utf-8-sig', index=False)

