
import pandas as pd
Pr
df = pd. read_csv ("data/tfidf-2024.cs") [["filename-1", "filename-2", "similarity
edges_df = df.rename (columns=("filename-1*: "Source" .
1.
"filename-2": "Target"
2.
"similarity": "Weight"ll
3.
edges_df.to_csv("outputs/mathew-barber-edges.csv", encoding="utf-B-sig",
index=False)
print (edges df)
nodesI = aETC"Ealename-1"， "titie-1"11
nodes1 - nodesl, renane (columns-("(ilenane-1"= "Id",
"t1t10-1："Lahel"］）
nodes2 = dfII"cilename-2", "titTo=2ª]]
hodes2 = nodes2. rename (columns-l"Cilename 2": Ld*
"title-2':"Label"l)
nodes = pd.concat ([nodesi, nodes2])
