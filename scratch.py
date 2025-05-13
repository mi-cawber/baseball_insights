import requests, bs4



 
res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
contents = soup.select('td .number, td .letter') # captures data in Tag format

# transfers Tag data into array
def data_transfer(raw, array):
    blacklist = ['Player', 'Games', 'At Bats', 'Runs', 'Hits',
                 'HR', 'RBI', 'BB', 'K', 'BA', 'OBA', 'Slug%',
                 'Last Game Date', '']
    for element in raw:
        if element.getText() in blacklist:
            continue
        else:
            array.append(element.getText())

# shows data array
def print_array(array):
    print(f'The length of the array is: {len(array)}', '\n')
    for element in array:
        print(element)