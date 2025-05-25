'''
This functions in this file generate 
insights of interest using the collected data.
'''
import pandas as pd


# this will print the current win percentages, according to the latest data
def win_pct():
    standings = pd.read_csv('standings_2025.csv')
    win_pct = standings[['Team', 'Win Pct', 'Date Collected']]
    win_pct = win_pct.tail(30)
    win_pct = win_pct.sort_values(['Win Pct'], ascending=False)
    print(win_pct)


# displays the current standings, according to the latest data
def standings():
    standings = pd.read_csv('standings_2025.csv') # standings dataframe
    # first set of brackets accesses dataframe, second set is list of columns
    standings = standings[['Team','Record','Date Collected']]
    print(standings.tail(30)) # 30 teams

# this will display the top hit streak leaders
def highest_hit_streaks():
    hit_streaks = pd.read_csv('hit_streaks_2025.csv')
    # drop all columns except player, streak count
    trimmed_streaks = hit_streaks[['Player', 'Games', 'Date Collected']]
    # this sorts the data by highest hits
    max_streaks = trimmed_streaks.sort_values(['Games'], ascending=False)
    # this drops duplicates of player, leaving only their highest streak
    max_streaks = max_streaks.drop_duplicates(['Player'])
    print(max_streaks)