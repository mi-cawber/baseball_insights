import requests as req # captures webpages
import bs4 # parses html?

# use baseballmusings.com, returns Response object
res = req.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

# takes text of Response object and returns BeautifulSoup object
# needed for BeautifulSoup.select()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# captures wanted elements using CSS selector?
elems = soup.select('#body > table > tbody > tr:nth-child(2) > td:nth-child(1) > table')

print(len(elems))

# Selector for the table
#body > table > tbody > tr:nth-child(2) > td:nth-child(1) > table