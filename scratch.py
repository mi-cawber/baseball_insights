import requests, bs4

# get hit streak data from web
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
raw_contents = soup.select('.letter, .number') # captures data

for element in raw_contents:
   
    print(f'{element.get_text()}', end=',') #THIS FUCKING DOES IT
