import pandas as pd
import plotly.express as px
import os

# Load tfidf matrix
df = pd.read_csv('data/tfidf-2024.csv')

# Step 1: Create Edges List
edges = df.rename(columns={
    'filename-1': 'Source',
    'filename-2': 'Target',
    'similarity': 'Weight'
})[['Source', 'Target', 'Weight']]

# Step 2: Extract nodes from both source and target sides
source_nodes = df[['filename-1', 'title-1', 'month-1']].rename(
    columns={'filename-1': 'Id', 'title-1': 'Label', 'month-1': 'month'}
)
target_nodes = df[['filename-2', 'title-2', 'month-2']].rename(
    columns={'filename-2': 'Id', 'title-2': 'Label', 'month-2': 'month'}
)

# Combine and drop duplicates
nodes = pd.concat([source_nodes, target_nodes]).drop_duplicates()

# Ensure the output folder exists
os.makedirs('outputs', exist_ok=True)

# Step 3: Save CSV files with required encoding and without index
edges.to_csv('outputs/mahpara-karim-edges.csv', encoding='utf-8-sig', index=False)
nodes.to_csv('outputs/mahpara-karim-nodes.csv', encoding='utf-8-sig', index=False)



