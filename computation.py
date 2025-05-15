import pandas as pd, matplotlib as plt

df = pd.read_csv('hit_streaks.csv')

print(df['Player'].value_counts())

