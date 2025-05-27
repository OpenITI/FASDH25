import pandas as pd
import os

# Loading the tfidf data
df = pd.read_csv("data/tfidf-2024.csv")

# Renaming the required columns
df = df.rename(columns={
    'filename-1': 'Source',
    'filename-2': 'Target',
    'similarity': 'Weight'
})
# Creating Edges DataFrame
edges = df[['Source', 'Target', 'Weight']]

# Create Nodes DataFrame from both sides
nodes_source = df[['Source', 'title-1', 'month-1']].rename(columns={
    'Source': 'Id',
    'title-1': 'Label',
    'month-1': 'month'
})
nodes_target = df[['Target', 'title-2', 'month-2']].rename(columns={
    'Target': 'Id',
    'title-2': 'Label',
    'month-2': 'month'
})

# Combine and deduplicate
nodes = pd.concat([nodes_source, nodes_target], ignore_index=True).drop_duplicates(subset=['Id'])

# Write the CSVs to the output folder
edges.to_csv("outputs/Sarir_Ahmad-edges.csv", encoding='utf-8-sig', index=False)
nodes.to_csv("outputs/Sarir_Ahmad-nodes.csv", encoding='utf-8-sig', index=False)

print("Files created in the 'outputs' folder.")
