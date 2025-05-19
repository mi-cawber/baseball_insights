import pandas as pd

streaks = pd.read_csv('hit_streaks.csv')
print(type(streaks['Player']))
print(type(streaks['Player', 'Manny Machado']))