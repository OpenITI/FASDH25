#import libraries

import pandas as pd

#load the csv file
df = pd.read_csv("data/tfidf-2024.csv")


#create the edges list
edges_df = df.rename(columns={"filename-1": "Source",
                              "filename-2": "Target",
                              "Similarity": "Weight"})

edges_df = edges_df[["Source", Target", "Weight"]]
print(edges_df)
edges_df.to_csv("outputs/Zehrish-Iqbal-edges.csv", encoding="utf-8-sig",
                index=False)


source_nodes = df.renamed(columns={"filename-1": "Id",
                                   "title-1": "Lable",
                                   "month-1": "month"})
source_nodes = source_nodes[["Id", "Label", "month"]]

target_nodes = df.rename(columns={"filename-2": "Id",
                                  "title-2": "Label",
                                  "month-2": "month"{)

target_notes = target_notes[["Id", "Label", "month"]]

nodes = pd.concat([source_nodes, target_nodes])
                                  
nodes = nodes.drop_duplicates()

print(nodes)                                 

nodes.to_csv("outputs/Zehrish-Iqbal-nodes.csv",encoding="utf-8-sig",
             index=False)
                              
