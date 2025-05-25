# https://docs.google.com/presentation/d/1i5Ro-QSz5tZ_0kr-UyJ0VqFzu1wg6kC1bbsYXKrXIDE/edit?slide=id.p#slide=id.p

# Titles (of books, articles &c.) are the best way to grasp the literary field
# as a whole. They're not just a key research tool. They matter intrinsically.
# Titles are chosen with deliberate care, acting as coded messages.

# 1 - Material - AJE articles on Palestine
# 2 - Processing - identifying topics and frequent terms (using TF-IDF and other methods
#                - a form of distant reading (as opposed to close reading of texts)
# 3 - Presentation(graphs) - shows change over time in the frequency of word usage
#                          - helps identify themes and proportionality of subject matter


import pandas as pd
import plotly.express as px

df=pd.read_csv('data/topic-model.csv')

print (df.columns)

print('---------')

pd.set_option('display.max_rows', None)
print (df[['Topic','topic_1', 'topic_2','topic_3','topic_4']].drop_duplicates())

df['topic_label']=df['Topic'].map(topic_labels)


1 On releasing hostages held by Hamas (captives, hamas, release, hostages)
5 People killed in Khan Younis (South Gaza 'safe-zone') (gaza, people, killed, younis)
6 Houthis retaliate in the Red Sea (houthis, houthi, sea, yemen)
18 Police brutality against pro-Palestinian protestors (protestors, palestine, police, protest)
35 Aid shortages worsen famine in Gaza civilians (aid, food, famine, Gaza)
24 Israeli rockets target Gaza (rockets, israeli, gaza, in)
36 European countries send aid to Gaza(eu, european, for, aid)
58 Children held in Israeli detention (detention, prisoners, are, children)
73 AI used to target civilians in Gaza (ai, technology, kil, civilians)

-1 the, to, of, and
79 we, are, to, is

#fig=px.bar

## show the counts of articles for at least 5 topics,
## using separate bars for counts of articles by the year it was published

##Write three sentences describing what you learn from
##producing a bar chart of those topics

