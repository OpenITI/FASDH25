import pandas as pd
import os

# Ensure that output directory exists
os.makedirs('outputs', exist_ok=True)

# Correct: Do NOT use index_col=0
df = pd.read_csv('data/tfidf-2024.csv')

# 1. Create the edges list
edges = df[['filename-1', 'filename-2', 'similarity']]
edges.columns = ['Source', 'Target', 'Weight']

# 2. Create the nodes list
source_nodes = df[['filename-1', 'title-1', 'month-1']]
source_nodes.columns = ['Id', 'Label', 'month']

target_nodes = df[['filename-2', 'title-2', 'month-2']]
target_nodes.columns = ['Id', 'Label', 'month']

# Combine and remove any duplicate nodes that still exists
nodes = pd.concat([source_nodes, target_nodes]).drop_duplicates(subset='Id')

# 3. Save to a CSV file
edges.to_csv('outputs/Zeeshan-Karim.csv', encoding='utf-8-sig', index=False)
nodes.to_csv('outputs/Zeeshan-Karim.nodes.csv', encoding='utf-8-sig', index=False)

