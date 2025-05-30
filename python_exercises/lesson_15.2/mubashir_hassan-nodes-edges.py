import pandas as pd

df = pd.read_csv("data/tfidf-2024.csv")

edges_df = df.rename(columns= {"filename-1": "source",
                               "filename-2": "Target",
                               "similarity": "Weight"))

edges_df = edges_df[["source", "Target", "Weight"]]
print(edges_df)
edges_df.to_csv("output/mubashir-hassan-edges.csv", encoding="utf-8-sig", index=False

source_nodes = df.renamed(columns={"filename-1": "Id",
                                   "title-1": "Label",
                                   "month-1": "month"})
source_nodes = target_nodes[{

nodes = pd.concat([source_nodes, target_nodes])
nodes = nodes.drop_duplicates()
