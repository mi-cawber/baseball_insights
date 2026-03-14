<img src='photos/baseball_player.png' alt='baseball player' style='width: 100px; height: 90px'>

# baseball_insights
The goal of this project is to collect, store, and perform calculations on baseball data.

# Libraries Used
[requests](https://pypi.org/project/requests/): Used for pulling data from the web. <br>
e.g., <br>
`res = requests.get(url) # grabs html from url`<br>

[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/): Used for parsing HTML data that was pulled by requests.
<br>
e.g., <br>
`soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object` <br>
`raw = soup.select('td .number, td .letter') # returns Tag object` <br>

[pandas](https://pandas.pydata.org/docs/): Used for computational operations on retrieved data.

# Database
[SQLite](https://sqlite.org/index.html): Version 3.51.2

# Data Sources
[Lahman Database](https://sabr.org/lahman-database/)
[Baseball Reference](https://www.baseball-reference.com/)
