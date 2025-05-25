import insights as i, pandas as pd
'''
-read in file, check last column, last row

-see if it matches current date (if it does, abort)

-if it doesn't, there's some work to do

-see when the last recorded date was

'''

df = pd.read_csv('world_series.csv')

df = df['Winning team']

print(df.mode())


