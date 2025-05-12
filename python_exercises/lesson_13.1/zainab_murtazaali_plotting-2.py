

import pandas as pd
import plotly.express as px

# Load the data
csv_path = "data/title.csv"
df = pd.read_csv(csv_path)

# Convert 'month' and 'year' to integers (in case they are not)
df['month'] = df['month'].astype(int)
df['year'] = df['year'].astype(int)

# 1. Histogram: Articles shorter than 300 words, colored by year
df_short = df[df['length'] < 300]

fig1 = px.histogram(df_short, x="length", color="year",
                    title="Article Lengths < 300 Words (Colored by Year)",
                    labels={"length": "Length in tokens", "year": "Year"},
                    color_discrete_map={2024: "Lightgreen", 2023: "orange", 2022: "Lightblue"})

fig1.add_annotation(x=150, y=50, text="Many short articles around 150 tokens",
                    showarrow=True, arrowhead=2, bgcolor="white")
fig1.show()

# 2. Histogram: Articles from 2023 and 2024 only
df_recent = df[df['year'].isin([2023, 2024])]

fig2 = px.histogram(df_recent, x="length", color="year",
                    title="Article Lengths from 2023 and 2024",
                    labels={"length": "Length in tokens", "year": "Year"},
                    color_discrete_map={2024: "Lightgreen", 2023: "orange"})

fig2.add_annotation(x=500, y=60, text="Interesting cluster of 2024 articles",
                    showarrow=True, arrowhead=1, bgcolor="white")
fig2.show()

# 3. Histogram: Articles from Oct–Dec 2023, colored by month
df_oct_dec = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

fig3 = px.histogram(df_oct_dec, x="length", color="month",
                    title="Article Lengths from Oct–Dec 2023 (Colored by Month)",
                    labels={"length": "Length in tokens", "month": "Month"},
                    color_discrete_sequence=px.colors.qualitative.Set2)

fig3.add_annotation(x=250, y=40, text="Spike in December articles",
                    showarrow=True, arrowhead=2, bgcolor="white")
fig3.show()
