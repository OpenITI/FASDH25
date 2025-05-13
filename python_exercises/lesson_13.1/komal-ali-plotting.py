import pandas as pd
import plotly.express as px
df = pd.read_csv("data/title.csv")

# print the head of the dataframe
print(df.head())

#Plot histogram with title and new xaxis label
fig = px.histogram(df, x = "length",
                   title = "Article lengths in the Gaza corpus",
                   labels= {"length": "Length in tokens"})

#Add ticks marks to the xaxis
fig.update_xaxes(ticks= "inside", tickwidth = 2)

fig.update_yaxes(title_text= "Frequency")

fig.show()
