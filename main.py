import requests, bs4

# returns Response object
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

# returns BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# captures table entries
table_contents = soup.select('td') # table rows


#first player data is contained from [3]-[14], 13 elements per
#second is [15]-[28]
print(table_contents[28].getText())
# add contents to data.csv file