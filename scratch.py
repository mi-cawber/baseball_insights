import requests, bs4
with open('data.csv', 'w') as file:

    # returns Response object
    res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

    # returns BeautifulSoup object
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # captures table entries
    table_header = soup.select('th') # table headers
    table_contents = soup.select('tr') # table rows


    # could be this simple to add

    x = 0
    while x <= 12:
        file.write(f'{table_header[x].getText()}' + ',')
        x += 1