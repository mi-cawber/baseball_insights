import retrieval as r, insights as i

# to collect hit streak data
# r.date_checker is ran before trying to receive data....
r.date_checker('hit_streaks_2025.csv', 'hit streak')
# that URL is where I get hit streak data from
raw, list = r.retrieve_data('https://www.baseballmusings.com/cgi-bin/CurStreak.py')
r.Tag_to_list(raw, list) # transfers Tag data to list
r.list_csv(list,'hit_streaks_2025.csv') # import into csv file

# to collect standings data
r.date_checker('standings_2025.csv', 'standings')
# that url is where I get standings data from
raw, list = r.retrieve_data('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025')
r.data_transfer(raw, list)
r.list_csv(list,'standings_2025.csv')

