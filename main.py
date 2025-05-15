import retrieval_functions as f

f.date_checker()
raw, array = f.retrieve_data('https://www.baseballmusings.com/cgi-bin/CurStreak.py')
f.data_transfer(raw, array) # transfers Tag data to array
f.array_csv(array,'hit_streaks.csv') # import into csv file
