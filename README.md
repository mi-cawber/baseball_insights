<img src='photos/baseball_player.png' alt='baseball player' style='width: 100px; height: 90px'>

# baseball_insights
The goal of this program is to collect baseball data from the internet and generate
potentially interesting insights. For example, seeing which players are consistently on hitting streaks.

# Libraries Used
[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/): Used for retrieving baseball stats from the web.
<br>
`res = requests.get(url) #returns response object` <br>
`soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object` <br>
`raw = soup.select('td .number, td .letter') # captures data in Tag format` <br>
`list = [] # to store data` <br>
`return raw, list`

[pandas](https://pandas.pydata.org/docs/): Used for computational operations on retrieved data.