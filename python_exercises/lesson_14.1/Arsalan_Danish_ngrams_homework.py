import pandas as pd
import plotly.express as px

# Quick sanity check – load up the dataset
data_path = 'data/1-gram.csv'
df = pd.read_csv(data_path)
print(df.head())  # Just making sure it loaded properly

# Pulled from NLTK – a decent base of common stopwords
#  might revisit and tweak this list depending on results
custom_stopwords = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
    'you', 'your', 'yours', 'yourself', 'yourselves',
    'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself',
    'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
    'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below',
    'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
    'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
    'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
    'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
    'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just',
    'don', 'should', 'now'
}

# Filtering out common stopwords so we focus on meaningful content words
df = df[~df['1-gram'].isin(custom_stopwords)]

# Let's find out which unigrams dominate the dataset
# Could use this as a sanity check before diving deeper
top_unigrams = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()
print("Top 5 unigrams:", top_unigrams)

# Zero in on just the top 5 for visualization purposes
df_top5 = df[df['1-gram'].isin(top_unigrams)].copy()

# Merging year, month, and day into a single datetime column
# I kept the day even though we'll mostly look at monthly trends
df_top5['date'] = pd.to_datetime(df_top5[['year', 'month', 'day']])

# Roll things up to a monthly level (aggregated count per unigram per month)
df_monthly = df_top5.groupby([df_top5['date'].dt.to_period('M'), '1-gram'])['count'].sum().reset_index()

# Convert back to timestamp format for plotting
df_monthly['date'] = df_monthly['date'].dt.to_timestamp()

# Plotting time! Using Plotly 
fig = px.line(
    df_monthly,
    x="date",
    y="count",
    color="1-gram",
    title="Monthly Frequency Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "date": "Month"},
    markers=True  # I like having dots on the lines – makes trends more visible
)

fig.show()  

# Save the chart in case we want to embed it or share it later
fig.write_html("top5_unigrams_trend.html")
