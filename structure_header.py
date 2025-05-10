import requests, bs4
# this created the header for  data.csv
with open('data.csv', 'w') as file:
    # returns Response object
    res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')
    # returns BeautifulSoup object
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # captures table entries
    table_header = soup.select('th') # table headers
    x = 0
    while x <= 12:
        if x == 12:
            file.write(f'{table_header[x].getText()}') #so there isn't the extra comma at the end
            break
        file.write(f'{table_header[x].getText()}' + ',')
        x += 1
    file.write(',Date Collected') # add row for date
    file.write('\n') # do a newline at the end