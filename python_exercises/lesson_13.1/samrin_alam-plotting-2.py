# Import the necessary libraries
import pandas as pd
import plotly.express as px

# read the data file
df = pd.read_csv("data/title.csv")

# print head of the data frame
print(df.head())



# Filter data frame for articles shorter than 300 words
df_short = df[df["length"] < 300]

# Create a histogram showing article lengths under 300
fig1 = px.histogram(df_short, x="length", color="year",
                    title="Articles under 300 words (by Year)",
                    labels={"length": "Article Length (words)", "year": "Year"})

# Set y-axis label to show it's frequency/count
fig1.update_yaxes(title="Frequency")

# Save the graph as an interactive HTML file
fig1.write_html("outputs/Samrin-Alam-short-articles.html")

# Show the plot
fig1.show()



#Histogram of articles lengths from the year 2023 and 2024 



# Filter articles from years 2023 and 2024
df_years = df[df["year"].isin([2023, 2024])]

# Create histogram for these years, colored by year
fig2 = px.histogram(df_years, x="length", color="year",
                    title="Articles from 2023 and 2024 (by Length)",
                    labels={"length": "Article Length (words)", "year": "Year"})

# Add annotation 
fig2.add_annotation(x=500, y=30,
                    text="Spike in article length around 500 words",
                    showarrow=True,
                    arrowhead=1)


fig2.update_yaxes(title="Frequency")
fig2.write_html("outputs/Samrin-Alam-articles-2023-2024.html")

# Show the plot
fig2.show()





# Filter data for articles in Octuber, November, December 2023

df_q4 = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

# Create histogram colored by month
fig3 = px.histogram(df_q4, x="length", color="month",
                    title="Article Lengths in Oct–Dec 2023 (by Month)",
                    labels={"length": "Article Length (words)", "month": "Month"})

# Add annotation to highlight a cluster of short articles
fig3.add_annotation(x=250, y=20,
                    text="Many short articles ~250 words",
                    showarrow=True,
                    arrowhead=1)

# Set y-axis label
fig3.update_yaxes(title="Frequency")

# Save the plot
fig3.write_html("outputs/Samrin-Alam-Q4-2023.html")

# Show the final plot
fig3.show()
