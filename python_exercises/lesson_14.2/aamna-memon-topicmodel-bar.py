# https://docs.google.com/presentation/d/1i5Ro-QSz5tZ_0kr-UyJ0VqFzu1wg6kC1bbsYXKrXIDE/edit?slide=id.p#slide=id.p
# Titles (of books, articles &c.) are the best way to grasp the literary field
# as a whole. They're not just a key research tool. They matter intrinsically.
# Titles are chosen with deliberate care, acting as coded messages.

# 1. Material - AJE articles on the genocide of Palestinians
# 2. Processing - identifying topics and frequent terms (using TF-IDF and other methods
#                - a form of distant reading (as opposed to close reading of texts)
# 3. Presentation(graphs) - shows change over time in the frequency of word usage
#                          - helps identify themes/proportionality of subject matters

import pandas as pd
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
print(counts)

import plotly.express as px
fig=px.bar(
    counts,
    x='year',
    y='yearly_count',
    color='Topic_Label',
    barmode='group',
    title='Topic Frequencies by Year',
    labels={
        'yearly_count':'Number of Articles',
        'year':'Year',
        'Topic_Label':'Topic'} )

fig.show()



'''
RESULTS:

Aid shortages increase over time. From 2023 to 2024, there is a stark rise in reporting
on this issue.
AI is not discussed at all in 2022, and overall reporting on the Palestinian issue
declines in 2022 across all topics.
Reports on police brutality decrease in 2024, likely due to a smaller dataset for
that year or possibly because protests declined. If so, this may indicate a loss of
faith in institutions or a general desensitization to the ongoing genocide.
Articles on 'Israeli rockets target Gaza' decline from 2023 to 2024, likely due to the
smaller number of articles available for 2024. Interestingly, reporting on Houthi
retaliation shows a steady increase.


Reference for topic words and assigned labels:
1:  On releasing hostages held by Hamas
    (captives, hamas, release, hostages)
5:  People killed in Khan Younis(South Gaza 'safe-zone')
    (gaza, people, killed, younis)
6:  Houthis retaliate in the Red Sea
    (houthis, houthi, sea, yemen)
18: Police brutality against pro-Palestinian protestors
    (protestors, palestine, police, protest)
35: Aid shortages worsen famine in Gaza civilians
    (aid, food, famine, Gaza)
24: Israeli rockets target Gaza
    (rockets, israeli, gaza, in)
36: European countries send aid to Gaza
    (eu, european, for, aid)
58: Children held in Israeli detention
    (detention, prisoners, are, children)
73: AI used to target civilians in Gaza
    (ai, technology, kill, civilians)


COMMENTS ON THE DATASET

The dataset appears unncesarily large, likely because it was not filtered for stopwords.
Examples:
-1: the, to, of, and
 2: my, her, she, we
 79: we, are, to, is

Some topic words do not clearly reflect the article subjects, likely due to the presence
of stopwords or vague terms.
Examples:
 7: netanyahu, government, the, to
23: tunnels, tunnel, hamas, be
33: church, christians, christian, christmas
41: brazil, lula, foreign, brazilian

Cleaning the data - such as removing stopwords, lemmatizing words (e.g., combining
brazil and brazilian), and reducing words to their singular forms (e.g., christian and
christians) - would help improve clarity and accuracy for topic modeling.
'''

