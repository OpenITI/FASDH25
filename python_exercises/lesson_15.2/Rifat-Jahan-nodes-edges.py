import pandas as pd
df = pd.read_csv("data/tfidf-2024.csv")
#creating the edges list
edges_df = df.rename(columns={
    'filename-1': 'Source',
    'filename-2': 'Target',
    'similarity': 'Weight'
})[['Source', 'Target', 'Weight']]
# Creating the nodes list  
# Combining both sides to get all unique filenames, titles, and months
nodes_1 = df[['filename-1', 'title-1', 'month-1']].rename(columns={
    'filename-1': 'Id',
    'title-1': 'Label',
    'month-1': 'month'
})

nodes_2 = df[['filename-2', 'title-2', 'month-2']].rename(columns={
    'filename-2': 'Id',
    'title-2': 'Label',
    'month-2': 'month'
})

nodes_df = pd.concat([nodes_1, nodes_2]).drop_duplicates(subset='Id')

 #Save to CSV files  
first = "Rifat"   
last = "Jahan"    

edges_df.to_csv(f"outputs/{Rifat}-{Jahan}-edges.csv", encoding='utf-8-sig', index=False)
nodes_df.to_csv(f"outputs/{Rifat}-{Jahan}-nodes.csv", encoding='utf-8-sig', index=False)
