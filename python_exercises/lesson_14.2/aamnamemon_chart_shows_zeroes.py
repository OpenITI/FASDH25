import pandas as pd
import plotly.express as px
df=pd.read_csv('data/topic-model.csv')
print (df.columns)
print('\n---------\n')


pd.set_option('display.max_rows', None)
print (df[['Topic','topic_1', 'topic_2','topic_3','topic_4']].drop_duplicates())
print('\n--------\n')

topic_labels={
    1:'On releasing hostages by Hamas',
    5:'People killed in Khan Younis (Gaza`s safe-zone)',
    6:'Houthis retaliate in the Red Sea',
    18:'Police brutality against pro-Palestinian protestors',
    35:'Aid shortages worsen famine in Gazan civilians',
    24:'Israeli rockets target Gaza',
    36:'European countries send aid to Gaza',
    58:'Children held in Israeli detention',
    73:'AI used to target civilians in Gaza'}


df['Topic_Label']=df['Topic'].map(topic_labels)
labeled_rows=df[df['Topic_Label'].notna()]
print (labeled_rows)
print('\n--------------\n')

counts=labeled_rows.groupby(['year','Topic_Label']).size().reset_index(name='yearly_count')

all_years=df['year'].unique()
all_topics= list(topic_labels.values())
full_grid=pd.MultiIndex.from_product([all_years, all_topics],names=['year', 'Topic_Label']).to_frame(index=False)

full_counts=pd.merge(full_grid, counts, on=['year', 'Topic_Label'],how='left')
full_counts['yearly_count']=full_counts['yearly_count'].fillna(0).astype(int)

print(full_counts)

fig=px.bar (
    full_counts,
    x='year',
    y='yearly_count',
    color='Topic_Label',
    barmode='group',
    title='Topic Frequencies by Year',
    text=full_counts['yearly_count'].apply(lambda x:'0' if x==0 else ''),
    labels={
        'yearly_count':'Number of Articles',
        'year':'Year',
        'Topic_Label':'Topic'}
    )
fig.update_traces(textposition='outside', cliponaxis=False)
fig.show()
