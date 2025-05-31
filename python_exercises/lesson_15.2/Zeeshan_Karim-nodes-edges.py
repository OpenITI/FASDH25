import pandas as pd

# Load the similarity data from CSV
df = pd.read_csv('data/tfidf-2024.csv', index_col=0)

# Reset the index so 'filename-1' becomes a regular column
df = df.reset_index()

# #Create the edges list
# #Select the relevant columns for the edges: source, target, and similarity score
edges_df = df.rename(coulmns= {"filename-1": "Source",
                               "filename-2": "Target"
                               "similarity": "weight"})
edges_df = edges_df[["Source" ,"Target", "Weight"]]
print(edges_df)
edges_df.to_csv("outputs/Zeeshan-karim-edges.csv", encoding= "utf-8-sig", index=False)

souce_nodes = df.renamed(columns={"filename-1":"Id",
                                  "title-1": "Label",
                                  "month-1":"month"})
source_nodes = source_nodes[["Id", "Label" , "month"]]

target_nodes = df.rename(columns={"filename-1":"Id",
                                  "title-1": "Label",
                                  "month-1":"month"})

target_nodes = target_nodes[["Id", "Label" , "month"]]


nodes = pd.concat([source_nodes, target_nodes])
nodes = nodes.drop_duplicates()

print(nodes)
