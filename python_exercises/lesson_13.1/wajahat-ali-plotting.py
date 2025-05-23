#import libraries
import pandas as pd
import plotly.express as px

# loading csv data frame
data_path = "data/title.csv"

# read the csv dataframe
df = pd.read_csv(data_path)

#printing the heads of the dataframe
print(df.head())

# -------------------------------
# 1️⃣ Histogram of articles < 300 words by year
# -------------------------------

# Filter dataframe for articles with length < 300
df_short = df[df['length'] < 300]

# Create histogram
fig1 = px.histogram(df_short, x="length", color="year",
                    title="Article Lengths under 300 Words by Year",
                    labels={"length": "Length (tokens)", "count": "Frequency"})

# Customize axes
fig1.update_xaxes(ticks="outside", tickwidth=2, minor_ticks="outside", minor_tickwidth=2)
fig1.update_yaxes(title="Frequency")

# Save the plot to HTML
fig1.write_html("outputs/Wajahat-Ali-under-300.html")


# -------------------------------
# 2️⃣ Histogram for years 2023 and 2024, with annotation
# -------------------------------

# Filter dataframe for years 2023 and 2024
df_recent = df[df['year'].isin([2023, 2024])]

# Create histogram
fig2 = px.histogram(df_recent, x="length", color="year",
                    title="Article Lengths in 2023 and 2024",
                    labels={"length": "Length (tokens)", "count": "Frequency"})

# Add annotation (example: peak at length 500 tokens)
fig2.add_annotation(x=500, y=20,
                    text="Noticeable peak at 500 tokens",
                    showarrow=True, arrowhead=2)

# Customize axes
fig2.update_xaxes(ticks="outside", tickwidth=2, minor_ticks="outside", minor_tickwidth=2)
fig2.update_yaxes(title="Frequency")

# Save the plot to HTML
fig2.write_html("outputs/Wajahat-Ali-hist-2023-2024.html")


# -------------------------------
# 3️⃣ Histogram for Oct, Nov, Dec 2023 with annotation
# -------------------------------

# Filter dataframe for articles from Oct, Nov, Dec 2023
df_q4_2023 = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

# Create histogram
fig3 = px.histogram(df_q4_2023, x="length", color="month",
                    title="Article Lengths in Oct-Dec 2023",
                    labels={"length": "Length (tokens)", "count": "Frequency", "month": "Month"})

# Add annotation (example: cluster of short articles)
fig3.add_annotation(x=250, y=10,
                    text="Cluster of short articles",
                    showarrow=True, arrowhead=2)

# Customize axes
fig3.update_xaxes(ticks="outside", tickwidth=2, minor_ticks="outside", minor_tickwidth=2)
fig3.update_yaxes(title="Frequency")

# Save the plot to HTML
fig3.write_html("outputs/Wajahat-Ali-hist-oct-dec-2023.html")

# Done!
print("All plots generated and saved successfully.")
