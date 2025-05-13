import requests, bs4, functions

res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
raw = soup.select('td .number, td .letter') # captures data in Tag format
array = [] # to store data

for i in raw:
    array.append(i.getText())

array = array[:13]

with open('data.csv', 'a') as file:
    for i in array:
        file.write(f'{i},')
    file.write(f'Date Collected')