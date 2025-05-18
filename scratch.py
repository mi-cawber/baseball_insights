import pandas as pd

streaks = pd.read_csv('hit_streaks.csv')
print(streaks.mode())