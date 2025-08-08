import retrieval as r
import os

#for cron daemon. This will set the working directory as the project folder,
#so that relative paths can be used in functions.
os.chdir('/home/joshua/baseball_insights')

# hit streak data
r.scraping_pipeline('https://www.baseballmusings.com/cgi-bin/CurStreak.py', 'hit_streaks_2025.csv', 'hit streak')

# standings date
r.scraping_pipeline('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025', 'standings_2025.csv', 'standings')
