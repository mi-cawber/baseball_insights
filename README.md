<img src='photos/baseball_player.png' alt='baseball player' style='width: 100px; height: 90px'>

# baseball_insights
The goal of this program is to collect baseball data from the internet and generate
potentially interesting insights. For example, seeing which players are consistently on hitting streaks.

# Libraries Used
[requests](https://pypi.org/project/requests/): Used for pulling data from the web. <br>
e.g., <br>
`res = requests.get(url)`<br>

[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/): Used for retrieving baseball stats from the web.
<br>
e.g., <br>
`soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object` <br>
`raw = soup.select('td .number, td .letter') # returns data in type Tag` <br>
`list = [] # to store data` <br>

[pandas](https://pandas.pydata.org/docs/): Used for computational operations on retrieved data.
<br>
e.g.,<br>
`df = pd.read_csv('hit_streaks.csv') # create dataframe`<br>
`print(df['Player'].value_counts()) # print player frequencies`
