import pandas as pd

hit_streaks = pd.read_csv('hit_streaks.csv')
# drop all columns except player, streak count
trimmed_streaks = hit_streaks[['Player', 'Games']]
# this sorts the data by highest hits
max_streaks = trimmed_streaks.sort_values(['Games'], ascending=False)
# this drops duplicates of player, leaving only their highest streak
max_streaks = max_streaks.drop_duplicates(['Player'])
print(max_streaks)