import pandas as pd  
df = pd.read_csv("data/tfidf-2024.csv")[["filename-1", "filename-2", "similarity", "title-1", "title-2"]]

edges_df = df.rename(columns={"filename-1": "Source",
    "filename-2": "Target",
    "similarity": "Weight"})

edges_df.to_csv("outputs/muhammad-faheem-edges.csv", encoding="utf-8-sig",
    index=False)

print(edges_df)
nodes1 = df[["filename-1", "title-1"]]
nodes1 = nodes1.rename(columns={"filename-1": "Id",
    "title-1": "Label"})

nodes2 = df[["filename-2", "title-2"]]
nodes2 = nodes2.rename(columns={"filename-2": "Id",
    "title-2": "Label"})

nodes = pd.concat([nodes1, nodes2])
print(nodes)
nodes.to_csv("outputs/muhammad-faheem-nodes.csv", encoding="utf-8-sig",
    index=False)
