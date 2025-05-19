# Importing the libraries
import pandas as pd
import plotly.express as px

# Loading the CSV file 
df = pd.read_csv("data/1-gram.csv")

# Printing the first 10 rows 
print(df.head(10))

# Filtering: subset of the dataframe
filter = df["1-gram"].isin(["peace","agreement","truce"])

df2 = df[filter]

print(df2)

# Ploting line graph

# Step 1: Combine year, month, day into a datetime column
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

# Step 2: Create a "month" column 
df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()

# Step 3: Filter the unigrams you're interested in
df_filtered = df[df["1-gram"].isin(["peace", "agreement", "truce"])]

# Step 4: Group by month and unigram, summing counts
df_monthly = df_filtered.groupby(["month", "1-gram"], as_index=False)["count"].sum()

# Step 5: Plot the line chart
fig = px.line(
    df_monthly,
    x="month",
    y="count",
    color="1-gram",
    title="Monthly Frequency of Selected Unigrams",
    labels={"month": "Month", "count": "Frequency", "1-gram": "Unigram"}
)

fig.show()

