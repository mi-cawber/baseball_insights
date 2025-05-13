import requests, bs4

# get hit streak data from web
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
raw_contents = soup.select('td .number, td .letter') # captures data

print(len(raw_contents))
str(raw_contents[415])
print(raw_contents[415].attrs)
exit()
truncated_elements = raw_contents[2:]




for element in truncated_elements:
   
    print(f'{element.get_text()}', end=',') #THIS FUCKING DOES IT
