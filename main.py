import requests, bs4

# returns Response object
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

# returns BeautifulSoup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# captures table contents from web
raw_contents = soup.select('td') # table rows

# cuts irrelevant content
truncated_contents = raw_contents[2:457] # goes from [0]-[454]

print(truncated_contents[12].getText())
from datetime import datetime, date

today = date.today()
date_string = today.strftime("%Y-%m-%d")


def test():
    x=0
    while x <13:
        print(truncated_contents[x].getText())
        x +=1
    print(date_string)