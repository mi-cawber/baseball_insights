import pandas as pd, matplotlib as plt

df = pd.read_csv('hit_streaks.csv')

print(df.Games.describe()) # describe

print(df.Player.describe())

print(df.Player.asfreq())
frequencies = df['Games'].value_counts()
print(frequencies)