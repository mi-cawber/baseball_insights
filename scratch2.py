import requests, bs4, csv


# returns Response object
response = requests.get('https://www.fangraphs.com/leaders/major-league?pagenum=1&pageitems=2000000000')

# use bs4 to turn into BeautifulSoup object
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# select data we want using bs4.select()
# returns ResultSet
raw = soup.select('tr, td')

list = []

for e in raw:
    if e:
        list.append(e.getText().strip())


print(list)