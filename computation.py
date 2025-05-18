import pandas as pd


def current_standings():
    standings = pd.read_csv('standings.csv') # standings dataframe
    # first set of brackets accesses dataframe, second set is list of columns
    standings = standings[['Team','Record']]
    print(standings.tail(30)) # 30 teams

current_standings()