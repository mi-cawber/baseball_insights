import requests, bs4, csv

# returns Response object
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

# returns BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup.prettify()
# captures table entries
table_header = soup.select('th') # table headers
table_contents = soup.select('tr') # table rows

