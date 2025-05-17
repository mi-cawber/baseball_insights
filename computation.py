import pandas as pd, matplotlib as plt

streaks = pd.read_csv('hit_streaks.csv') # streak dataframe
#print(streaks['Player'].value_counts()) # print player frequencies
'''
standings = pd.read_csv('standings.csv') # standings dataframe
winpct = standings[['Team','Win Pct']] # double brackets? not sure why needed
winpct = winpct.sort_values('Win Pct', ascending=False) # highest pct at top


'''

standings = pd.read_csv('standings.csv')
record = standings[['Team', 'Record']]
record = record.sort_values('Record', ascending=False)
print(record)