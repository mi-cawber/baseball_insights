import retrieval as r

# hit streak data
r.scraping_pipeline('https://www.baseballmusings.com/cgi-bin/CurStreak.py', 'hit_streaks_2025.csv', 'hit streak')

# standings date
r.scraping_pipeline('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025', 'standings_2025.csv', 'standings')
