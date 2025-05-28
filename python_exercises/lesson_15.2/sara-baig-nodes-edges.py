import pandas as pd
#loading the data
df = pd.read_csv("data/tfidf-2024.csv")

#creating edges list
edge_df = df.rename(columns={"filename-1": "Source",
                              "filename-2": "Target",
                              "similarity": "Weight"})

edges_df = edges_df[["Source", "Target", "Weight"]]
print(edges_df)
edges_df.to_csv("outputs/sara-baig-edges.csv", encoding="utf-8-sig", index=False

source_nodes = df.rename(columns={"filename-1": "Id",
                                  "title-1": "Label",
                                  "month-1": "month"})
source_nodes = source_nodes[["Id", "Label", "month"]]

target_nodes = df.rename(columns=("filename-2": "Id",
                                  "title-2": "Label",
                                  "month-2": "month")
target_nodes = target_nodes[["Id", "Label", "month"]]

nodes = pd.concat([source_nodes, target_nodes])
nodes = nodes.drop_duplicates()

print(nodes)

nodes.to_csv(f'outputs/sara-baig-nodes.csv', encoding='utf-8-sig', index=False
