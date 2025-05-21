# import necessary libraries
import pandas as pd
import plotly.express as px

# load csv file
df = pd.read_csv("../lesson_14.1/data/1-gram.csv")
# write a code to print first 10 rows
print(df.head(10))

# sort the dataframe by frequency
df_sorted = df.sort_values(by='count', ascending=False)
print(df_sorted.head(10))


#filter data

filter = df["1-gram"].isin(["peace", "agreement", "truce"])
# .copy() is added to avoid SettingWithCopyWarning
df2 = df[filter].copy()
print(df2)

# combine year, month, and day to create a full date column
# This helps us sort or group by time later
df2["date"] = pd.to_datetime({
    "year": df2["year"],
    "month": df2["month"],
    "day": df2["day"]
})

# create a new column with just year and month
# we will use this to group by month
df2["month_year"] = df2["date"].dt.to_period("M")

# Group by month and 1-gram, and sum the counts
grouped = df2.groupby(["month_year", "1-gram"])["count"].sum().reset_index()

# Convert month_year back to a full date so we can plot it
grouped["month_year"] = grouped["month_year"].dt.to_timestamp()

# Plot the results
import plotly.express as px

fig = px.line(grouped, x="month_year", y="count", color="1-gram",
              title="Monthly Frequency of Selected 1-grams")
# save the figure
fig.write_html("abdus_salam_plot.html")

fig.show()
