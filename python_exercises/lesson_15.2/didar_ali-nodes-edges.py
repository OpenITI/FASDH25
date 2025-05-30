import pandas as pd

# Loading data
df = pd.read_csv('data/tfidf-2024.csv', index_col=0)

# Reset index to get 'filename-1' into columns
df = df.reset_index()

# Build the edges list
edges = df[['filename-1', 'filename-2', 'similarity']]
edges.columns = ['Source', 'Target', 'Weight']


# Extract source nodes
source_nodes = df[['filename-1', 'title-1', 'month-1']]
source_nodes.columns = ['Id', 'Label', 'month']

# Extract target nodes
target_nodes = df[['filename-2', 'title-2', 'month-2']]
target_nodes.columns = ['Id', 'Label', 'month']

# Combine and drop duplicates
nodes = pd.concat([source_nodes, target_nodes])
nodes = nodes.drop_duplicates(subset='Id')


# 3. Save to CSV
edges.to_csv(f'outputs/didar_ali-edges.csv', encoding='utf-8-sig', index=False)
nodes.to_csv(f'outputs/didar_ali-nodes.csv', encoding='utf-8-sig', index=False)
