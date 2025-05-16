import pandas as pd, matplotlib as plt

df = pd.read_csv('hit_streaks.csv') # create dataframe
print(df['Player'].value_counts()) # print player frequencies

