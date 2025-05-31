import pandas as pd

# Read the CSV file and select specific columns
df = pd.read_csv("data/ft1df-2024.csv")[["filename-1", "filename-2", "similarity"]]

# 1. Prepare edges dataframe
edges_df = df.rename(columns={
    "filename-1": "source",
    "filename-2": "target",
    "similarity": "height"
})

# Save edges to CSV
edges_df.to_csv("outputs/nathew-barber-edges.csv", encoding="utf-8-sig", index=False)
print(edges_df)

# 2. Prepare nodes dataframe
nodes1 = df[["filename-1", "title-1"]]
nodes1 = nodes1.rename(columns={
    "filename-1": "id",
    "title-1": "label"
})

nodes2 = df[["filename-2", "title-2"]]
nodes2 = nodes2.rename(columns={
    "filename-2": "id",
    "title-2": "label"
})

# Combine nodes
nodes = pd.concat([nodes1, nodes2])

# Save nodes to CSV
print(nodes)
nodes.to_csv("outputs/nathew-barber-nodes.csv", encoding="utf-8-sig", index=False)

