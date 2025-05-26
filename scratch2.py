import requests, bs4, csv


response = requests.get('https://www.baseball-reference.com/leagues/majors/2025-standard-batting.shtml')

print(response)


