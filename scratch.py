import requests, bs4

# get hit streak data from web
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
raw_contents = soup.select('td') # captures data
truncated_contents = raw_contents[2:456] # truncates irrelevant data (now range == [0]-[454])

for element in truncated_contents:
   
    print(f'{element.get_text()}', end=',') #THIS FUCKING DOES IT
