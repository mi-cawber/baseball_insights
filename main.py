'''
Main module, for running retrieval functions.
'''
import retrieval as r

# to collect hit streak data
r.date_checker('hit_streaks_2025.csv', 'hit streak')
raw, list = r.retrieve_data('https://www.baseballmusings.com/cgi-bin/CurStreak.py')
r.data_transfer(raw, list) # transfers Tag data to list
r.list_csv(list,'hit_streaks_2025.csv') # import into csv file

# to collect standings data
r.date_checker('standings_2025.csv', 'standings')
raw, list = r.retrieve_data('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025')
r.data_transfer(raw, list)
r.list_csv(list,'standings_2025.csv')