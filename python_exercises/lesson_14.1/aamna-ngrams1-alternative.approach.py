import pandas as pd
import plotly.express as px

df=pd.read_csv('data/1-gram.csv')

df['date']=pd.to_datetime({
    'year': df['year'],
    'month':df['month'],
    'day':1}
                           )

filter_list=['peace', 'agreement','truce']
df2=df[df['1-gram'].isin(filter_list)]

group=df2.groupby(['date', '1-gram'], as_index=False)['count'].sum()

fig=px.line(group,
            x='date',
            y='count',
            color='1-gram',
            markers=True)

fig.show()

# alternatively: use a bar plot:
fig = px.bar(group, x="date", y="count", color="1-gram", barmode="group")
fig.show()
