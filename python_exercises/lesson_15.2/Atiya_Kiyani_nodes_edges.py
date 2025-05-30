import pandas as pd

# Load the data
df = pd.read_csv("data/tfidf-2024.csv")
print(df.columns.tolist())

# ---- Create edges list ----
edges = df.rename(columns={
    'filename-1': 'Source',
    'filename-2': 'Target',
    'similarity': 'Weight'
})[['Source', 'Target', 'Weight']]

# ---- Create nodes list ----

# Extract nodes from filename-1
nodes_1 = df[['filename-1', 'title-1', 'month-1']].rename(columns={
    'filename-1': 'Id',
    'title-1': 'Label',
    'month-1': 'month'
})

# Extract nodes from filename-2
nodes_2 = df[['filename-2', 'title-2', 'month-2']].rename(columns={
    'filename-2': 'Id',
    'title-2': 'Label',
    'month-2': 'month'
})

# Combine and drop duplicates
nodes = pd.concat([nodes_1, nodes_2]).drop_duplicates(subset='Id')

# ---- Save files ----
first = "Atiya"
last = "Kiyani"

edges.to_csv(f"outputs/{first}-{last}-edges.csv", encoding='utf-8-sig', index=False)
nodes.to_csv(f"outputs/{first}-{last}-nodes.csv", encoding='utf-8-sig', index=False)

print("Nodes and edges files have been saved.")
