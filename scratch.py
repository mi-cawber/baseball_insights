import requests, bs4
from datetime import datetime, date

with open('data.csv', 'a') as file:

    # current date variable
    today = date.today()
    date_string = today.strftime("%Y-%m-%d")
    
    # get hit streak data from web
    res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
    soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
    raw_contents = soup.select('td') # captures data
    truncated_contents = raw_contents[2:457] # truncates irrelevant data (now range == [0]-[454])
    print(truncated_contents[12].getText())
    from datetime import datetime, date


    x=0    
    while x <13:
        print(f'{truncated_contents[x].getText()},')
        x +=1
    print(date_string)