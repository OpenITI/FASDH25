import pandas as pd
# Load the data
df = pd.read_csv('data/tfidf-2024.csv')

# Create edges list
edges = df.rename(columns={
    'filename-1': 'Source',
    'filename-2': 'Target',
    'similarity': 'Weight'
})[['Source', 'Target', 'Weight']]

# Create nodes list
# Combine both Source and Target to get unique filenames
all_filenames = pd.concat([edges['Source'], edges['Target']]).unique()

# Filter original df to keep only one row per filename to extract title and month
# Assumes 'filename', 'title', and 'month' columns exist in tfidf-2024.csv
node_info = df[['filename-1', 'title-1', 'month-1']].rename(columns={
    'filename-1': 'Id',
    'title-1': 'Label',
    'month-1': 'month'
}).drop_duplicates(subset='Id')

# If there are nodes missing (in Target but not in Source), we may need to do the same for filename-2
extra_info = df[['filename-2', 'title-2', 'month-2']].rename(columns={
    'filename-2': 'Id',
    'title-2': 'Label',
    'month-2': 'month'
}).drop_duplicates(subset='Id')

# Combine and drop duplicates again
nodes = pd.concat([node_info, extra_info]).drop_duplicates(subset='Id')

# Save outputs
edges.to_csv('outputs/zainab-murtaza-edges.csv', encoding='utf-8-sig', index=False)
nodes.to_csv('outputs/zainab-murtaza-nodes.csv', encoding='utf-8-sig', index=False)

print("Files saved successfully.")
