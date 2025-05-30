import pandas as pd
df = pd.read_csv("data/tfidf-2024.csv")

# creating the edge list
edges_df = df.rename(columns={
    'filename-1': 'Source',
    'filename-2': 'Target',
    'similarity': 'Weight'
 })   

edges_df.to_csv("outputs/samrin_alam-edges.csv", encoding="utf-8-sig"
                index=false)
nodes1 = df.renamed(cloumn="filename-1": "Id",
                           "tiltle-1: "Lable1"})


nodes2 = df.renamed(cloumn="filename-2": "title-2",
                           "tiltle-1: "Lable1"})                    
