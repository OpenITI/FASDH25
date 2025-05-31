import os
import pandas as pd

# Ensure outputs folder exists
os.makedirs('outputs', exist_ok=True)

# Load data
df = pd.read_csv('data/tfidf-2024.csv', index_col=0)

# Reset index to get 'filename-1' into columns
df = df.reset_index()

# 1. Create the edges list
edges = df[['filename-1', 'filename-2', 'similarity']]
edges.columns = ['Source', 'Target', 'Weight']

# 2. Create the nodes list
source_nodes = df[['filename-1', 'title-1', 'month-1']]
source_nodes.columns = ['Id', 'Label', 'month']

target_nodes = df[['filename-2', 'title-2', 'month-2']]
target_nodes.columns = ['Id', 'Label', 'month']

nodes = pd.concat([source_nodes, target_nodes])
nodes = nodes.drop_duplicates(subset='Id')

# 3. Save to CSV
edges.to_csv('outputs/kamran-abid-edges.csv', encoding='utf-8-sig', index=False)
nodes.to_csv('outputs/kamran-abid-nodes.csv', encoding='utf-8-sig', index=False)

# Debug print
print("Edges created:", len(edges))
print("Nodes created:", len(nodes))
print("Files saved in 'outputs/' folder.")
