import pandas as pd
import plotly.express as px
csv_path = "data/title.csv"
df=pd.read_csv(csv_path)
print(df.head())
print(df.columns)
fig=px.histogram(df, x='length',
                 title="article length",
                 labels={"length":"length in tokens"})
fig.show()
                 
                
