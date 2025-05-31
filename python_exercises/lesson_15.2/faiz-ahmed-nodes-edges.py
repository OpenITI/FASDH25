import pandas as pd

# Load data
df = pd.read_csv('data/tfidf-2024.csv', index_col=0)

edges_df=df.rename(columns={"filename-1":"Source",
                            "filename-2":"Target",
                            "Similarity":"Weight"
})[["Source","Target","Weight"]]
print(edges_df)

edges_df.to_csv(f'outputs/faiz-ahmed-edges.csv', encoding='utf-8-sig', index=False)

#creating the nodes list , Extract source nodes
source_nodes = df.rename(columns={"filename-1":"Id",
                                  "title-1":"Label",
                                  "month-1":"month"})
source_nodes = source_nodes[["Id", "Label", "month"]]

target_nodes=df.rename(columns={"filename-1":"Id",
                                "title-1":"Label",
                                "month-1":"month"})
target_nodes=target_nodes[["Id", "Label", "month"]]
# Combine and drop duplicates
nodes = pd.concat([source_nodes, target_nodes])
nodes = nodes.drop_duplicates()
print(nodes)

nodes.to_csv(f'outputs/faiz-ahmed-nodes.csv', encoding='utf-8-sig', index=False)

