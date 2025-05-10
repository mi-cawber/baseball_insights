import requests, bs4

# returns Response object
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

# returns BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# captures table entries
table_contents = soup.select('tr') # table rows

# add contents to data.csv file