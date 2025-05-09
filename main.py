import requests as req # captures webpages
import bs4 # parses html?

# use baseballmusings.com, returns Response object
res = req.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py')

# takes text of Response object and returns BeautifulSoup object
# needed for BeautifulSoup.select()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# captures table entries
table_header = soup.select('th')
table_contents = soup.select('tr') # selects elements with <tr> tage which are the table elements


print(len(table_header))
for table_header in table_header:
    print(table_header.getText())
exit()

for elems in elems:
    print(elems.getText())

#print(len(elems))

#for tr in elems:
    #print(tr)
