import pandas as pd



def win_pct():
    standings = pd.read_csv('standings.csv')
    win_pct = standings[['Team', 'Win Pct', 'Date Collected']]
    win_pct = win_pct.tail(30)
    win_pct = win_pct.sort_values(['Win Pct'], ascending=False)
    print(win_pct)


def standings():
    standings = pd.read_csv('standings.csv') # standings dataframe
    # first set of brackets accesses dataframe, second set is list of columns
    standings = standings[['Team','Record','Date Collected']]
    print(standings.tail(30)) # 30 teams

standings()
win_pct()