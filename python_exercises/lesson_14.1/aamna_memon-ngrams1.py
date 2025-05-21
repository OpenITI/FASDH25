import pandas as pd
import plotly.express as px
csv_path='data/1-gram.csv'
df=pd.read_csv(csv_path)
print(df.head(10))
df=df.sort_values(by='count', ascending=False)
print(df.head(10))

filter_list=['peace','agreement','truce']
df2=df[df['1-gram'].isin(filter_list)]
print(df2)

# incorrect approach because months have not been grouped together
#fig=px.line(df2, x='month', y='count')
#fig.show()

df['date']=pd.to_datetime(dict(
    year=df['year'],
    month=df['month'],
    day=1
    )
)
df2=df[df['1-gram'].isin(filter_list)]

group=df2.groupby(['date','1-gram'], as_index=False)['count'].sum()

fig=px.line(group, x='date',y='count',color='1-gram', markers=True)
fig.show()

fig=px.bar(group, x='date', y='count', color='1-gram', barmode='group')
fig.write_html('output-aamna.html')
