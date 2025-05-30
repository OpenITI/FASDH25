# import necessary libraries

import pandas as pd

# load file
df = pd.read_csv("data/tfidf-2024.csv")
print(df.head())

edges_df = df.rename(columns={"filename-1": "Source",
                              "filrname-2": "Target",
                              "Similarity": "Weight"})

edges_df.to_csv("outputs/atiqa-rani-edges.csv", encoding="utf-8-sig",
                index=False)

nodes1 = df[["filename-1", "title-1"]]
nodes1 = nodes1.rename(columns={"filename-1": "Id",
                            "title-1": "Label"})  
nodes2 = df[["filename-2", "title-2"]]
nodes1 = nodes1.rename(columns={"filename-1": "Id",
                            "title-2": "Label"})

nodes = pd.concat([nodes1, nodes2])
nodes.to_csv("outputs/atiqa-rani-nodes.csv",encoding="utf-8-sig",
             index=False)
