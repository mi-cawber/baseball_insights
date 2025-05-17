import retrieval_functions as f

# to collect hit streak data
f.date_checker('hit_streaks.csv', 'hit streak')
raw, list = f.retrieve_data('https://www.baseballmusings.com/cgi-bin/CurStreak.py')
f.data_transfer(raw, list) # transfers Tag data to list
f.list_csv(list,'hit_streaks.csv') # import into csv file

# to collect standings data
f.date_checker('standings.csv', 'standings')
raw, list = f.retrieve_data('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025')
f.data_transfer(raw, list)
f.list_csv(list,'standings.csv')