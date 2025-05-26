import requests, bs4, csv


response = requests.get('https://www.fangraphs.com/leaders/major-league?pagenum=1&pageitems=2000000000')

print(response.text)


