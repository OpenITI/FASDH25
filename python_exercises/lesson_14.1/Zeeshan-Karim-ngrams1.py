#importing libraries
import pandas as pd
import plotly.express as px

# Load the CSV file into a Dataframe
df = pd.read_csv("data/1-gram.csv")

# Filter for specific 1-grams and keep only rows where word is "peace", "agreement" or "truce"
filtered = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[filtered].copy() #Make a copy of the filtered data
print(df2.head(10))  #print first 10 rows

# Combine year, month, and day into a proper date column
df2["date"] = pd.to_datetime({
    "year": df2["year"],
    "month": df2["month"],
    "day": df2["day"]
})

# Create a new column that has 'month_year' column (for grouping)
df2["month_year"] = df2["date"].dt.to_period("M")

# Group by month and word, and calculate total count for each word per month
grouped = df2.groupby(["month_year", "1-gram"])["count"].sum().reset_index()

# Convert 'month_year'into a normal date format, so that plotly can plot it correctly (datetime format)
grouped["month_year"] = grouped["month_year"].dt.to_timestamp()

# Plot a line chart showing how the usage of each word changes overtime
fig = px.line(grouped, x="month_year", #timeline on x-axis
              y="count",            # frequency on the y-axis
              color="1-gram",   # separate line by word
              markers=True,     # Adding dots on the line for better visibility
              title="Frequency of 'peace', 'agreement', and 'truce' Over Time")

# Show the graph
fig.show()
