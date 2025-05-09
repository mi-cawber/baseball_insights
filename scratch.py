import requests, bs4, csv

# returns Response object
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

# returns BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# captures table entries
table_header = soup.select('th') # table headers
table_contents = soup.select('tr') # table rows


# get details about table_header
# 0-12 is useful to me
x = 0

print(table_header[0].getText())