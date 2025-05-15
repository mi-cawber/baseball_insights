import retrieval_functions as f

f.date_checker('hit_streaks.csv')
raw, list = f.retrieve_data('https://www.baseballmusings.com/cgi-bin/CurStreak.py')
f.data_transfer(raw, list) # transfers Tag data to list
f.list_csv(list,'hit_streaks.csv') # import into csv file
