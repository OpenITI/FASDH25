import pandas as pd

df=pd.read_csv('data/tfidf-2024.csv', index_col=0)

df=df.reset_index()

edges_df=df.rename[['Filename-1','Filename-2','Similarity']]
edges.columns=['Source','Target','Weight']

source_nodes=df[['Filename-1','Title-1','Month-1']]
source_nodes.columns=['Id','Label','Month']

target_nodes=df[['filename-2', 'title-2', 'month-2']]
target_nodes.columns = ['Id', 'Label', 'month']

nodes = pd.concat([source_nodes, target_nodes])
nodes = nodes.drop_duplicates(subset='Id')

edges.to_csv(f'outputs/Shaharyar-Amin-edges.csv', encoding='utf-8-sig', index=False)
nodes.to_csv(f'outputs/Shaharyar-Amin-nodes.csv', encoding='utf-8-sig', index=False)
