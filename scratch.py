import requests, bs4

# get hit streak data from web
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
raw_contents = soup.select('td .number, td .letter') # captures data
data_array = [] # im gonna put the data in here, easier to manipulate




# transfers Tag data into array
def data_transfer():
    for element in raw_contents:
        array.append(element.getText())
        
# shows data array
def show_data_array():
    for element in array:
        print(element)

