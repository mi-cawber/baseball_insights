import requests, bs4
import scratch as s

res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
raw = soup.select('td .number, td .letter') # captures data in Tag format
array = [] # to store data 

s.data_transfer(raw, array) # transfers Tag data to array
s.print_array(array) # shows array