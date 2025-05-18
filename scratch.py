import pandas as pd

standings = pd.read_csv('standings.csv') # standings dataframe

standings['Date Collected'] = pd.to_datetime(standings['Date Collected'])

standings.sort_values(['Date Collected'], ascending=False)

print(standings)