
import pandas as pd
import plotly.express as px

# Read CSV
df = pd.read_csv("data/title.csv")

# 1. Histogram: lengths < 300, colored by year
short_articles = df[df["length"] < 300]
fig1 = px.histogram(short_articles, x="length", color="year", title="Article Lengths < 300 by Year")
fig1.update_layout(xaxis_title="Length", yaxis_title="Count")
fig1.show()

# 2. Histogram: 2023 and 2024 only
recent_articles = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(recent_articles, x="length", color="year", title="Article Lengths (2023-2024) by Year")
fig2.update_layout(xaxis_title="Length", yaxis_title="Count")

# Add annotation
fig2.add_annotation(x=500, y=10, text="Spike in longer articles", showarrow=True, arrowhead=1)
fig2.show()

# 3. Histogram: Oct-Dec 2023 only
q4_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(q4_articles, x="length", color="month", title="Article Lengths (Oct-Dec 2023) by Month")
fig3.update_layout(xaxis_title="Length", yaxis_title="Count")
fig3.show()
