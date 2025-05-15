import pandas as pd
import plotly.express as px

csv_path= r"C:/Users/DELL/Downloads/FASDH25/python_exercises/lesson_13.1/data/title.csv"

df = pd.read_csv(csv_path)

fig = px.histogram(df, x="length",
                   y="frequency", 
                   title = "Article length in Gaza corpus",
                   labels = {"lengths":"lengths in token"})
fig.updpate_xaxes(ticks = "inside", tickwidth = 2,
                minor_ticks= "inse", minor_tickwidth=2)

fig.update_yaxes(ticks = "outside", tickwidth = 2,
                minor_ticks= "outside", minor_tickwidth=2)

fig.show()




