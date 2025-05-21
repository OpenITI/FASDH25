import pandas as pd
csv_path='data/title.csv'
df=pd.read_csv(csv_path)

title_column=df[['title']]
print (title_column)

print('\n---------------\n')

max_length=df['length'].max()
title_of_longest=df[df['length']==max_length]['title'].values[0] 
print(title_of_longest)

print('\n---------------\n')

total_length=df['length'].sum()
print(total_length)

print('\n---------------\n')

df=df.sort_values(by='length', ascending=False)
print(df[['title']].head(20))

print('\n---------------\n')

df2=df[:20]
output_file='outputs/aamna-memon-top20.csv'
df2.to_csv(output_file, index=False, sep=',')
print('first csv saved in outputs')
print('\n---------------\n')


df['full_date']=df['year'].astype(str)+'-'+df['month'].astype(str)+'-'+df['day'].astype(str)
print(df[['full_date']])

print('\n-----------\n')

first_six_months=df[(df['year']==2023) & (df['month']>=1) & (df['month']<=6)]
print (first_six_months)
output_file='outputs/aamna-memon-6m2023.csv'
first_six_months.to_csv(output_file, index=False, sep=',')
print('second csv saved in outputs')

