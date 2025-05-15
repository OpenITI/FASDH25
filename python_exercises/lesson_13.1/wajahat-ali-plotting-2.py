# Import the necessary libraries
import pandas as pd
import plotly.express as px

# Load the CSV file into a pandas DataFrame 
#to work with tabular data for filtering and plotting
df = pd.read_csv("data/title.csv")

# Show the first few rows to understand the data structure
print(df.head())



#Script for Histogram of article lengths shorter than 300 words



# Filter only rows where article length is under 300 to focus on short articles
df_short = df[df["length"] < 300]

# Create a histogram showing article lengths under 300
# Colored by year to compare changes over time
fig1 = px.histogram(df_short, x="length", color="year",
                    title="Articles under 300 words (by Year)",
                    labels={"length": "Article Length (words)", "year": "Year"})

# Set y-axis label to show it's frequency/count
fig1.update_yaxes(title="Frequency")

# Save the graph as an interactive HTML file
fig1.write_html("outputs/Wajahat-Ali-short-articles.html")

# Show the plot
fig1.show()



#Histogram of articles lengths from the year 2023 and 2024 



# Filter articles from years 2023 and 2024
# We want to compare just these two years
df_years = df[df["year"].isin([2023, 2024])]

# Create histogram for these years, colored by year
fig2 = px.histogram(df_years, x="length", color="year",
                    title="Articles from 2023 and 2024 (by Length)",
                    labels={"length": "Article Length (words)", "year": "Year"})

# Add annotation to highlight something noticeable (e.g. spike)
fig2.add_annotation(x=500, y=30,
                    text="Spike in article length around 500 words",
                    showarrow=True,
                    arrowhead=1)

# Set y-axis title
fig2.update_yaxes(title="Frequency")

# Save as HTML file
fig2.write_html("outputs/Wajahat-Ali-articles-2023-2024.html")

# Show the plot
fig2.show()




#Histogram of article lengths only from OCT 10, NOV 11 and DEC 12 of 2023


# Filter data for articles in Oct (10), Nov (11), Dec (12) of 2023
# To explore seasonal trends at the end of 2023
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
fig3.write_html("outputs/Wajahat-Ali-OCT-NOV-DEC-2023.html")

# Show the final plot
fig3.show()


