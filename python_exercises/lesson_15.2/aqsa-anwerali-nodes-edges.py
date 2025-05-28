import pandas as pd

# Load data
df = pd.read_csv("data/tfidf-2024.csv")

# Edges list
edges_df = df.rename(columns={
    "filename-1": "Source",
    "filename-2": "Target",
    "similarity": "Weight"
})
edges_df = edges_df[["Source", "Target", "Weight"]]
edges_df.to_csv("outputs/aqsa-anwerali-edges.csv", encoding="utf-8-sig", index=False)

# Nodes list
nodes1 = df[["filename-1", "title-1", "month-1"]]
nodes2 = df[["filename-2", "title-2", "month-2"]]

nodes1 = nodes1.rename(columns={"filename-1": "Id", "title-1": "Label", "month-1": "month"})
nodes2 = nodes2.rename(columns={"filename-2": "Id", "title-2": "Label", "month-2": "month"})

nodes = pd.concat([nodes1, nodes2])
nodes = nodes.drop_duplicates(subset="Id")
nodes.to_csv("outputs/aqsa-anwerali-nodes.csv", encoding="utf-8-sig", index=False)

print(nodes)
