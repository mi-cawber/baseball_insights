import requests, bs4, csv
from datetime import date

# big boss function, receives data
def retrieve_data():
    res = requests.get('https://www.baseballmusings.com/cgi-bin/CurStreak.py') #returns response object
    soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
    raw = soup.select('td .number, td .letter') # captures data in Tag format
    array = [] # to store data
    return raw, array

# transfers Tag data into array
def data_transfer(raw, array):
    # we don't want these items in the array
    blacklist = ['Player', 'Games', 'At Bats', 'Runs', 'Hits',
                 'HR', 'RBI', 'BB', 'K', 'BA', 'OBA', 'Slug%',
                 'Last Game Date']
    for element in raw:
        # if the element is a member of the blacklist, skip
        if element.getText() in blacklist:
            continue
        # if okay, add to array
        else:
            array.append(element.getText())
    # get rid of pesky '\n's in player strings
    for i in range(len(array)):
        array[i] = array[i].strip()

# shows data array
def print_array(array):
    # show length
    print(f'The length of the array is: {len(array)}', '\n')
    for element in array:
        print(element)

# inserts data into csv
def array_csv(array, csv):
    # will be needed later
    today = date.today().strftime("%Y-%m-%d")
    # open file in append mode
    with open(csv, 'a') as file:
        # enumerate() gives index and value
        for index, element in enumerate(array):
            # if a player's name
            if element[0].isalpha():
                    # if first element of array
                    if index == 0:
                        file.write(f'{element},')
                        continue
                    else:
                        # add date added for previous row and newline to next
                        file.write(f'{today}\n{element},')
                        continue
            # add numerical data
            file.write(f'{element},')
        # this will print last
        file.write(f'{today}\n')

# checks if the function has been run today, will stop duplicate data
def date_checker():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        liszt = list(reader)
        liszt = liszt[-1][-1] #last element of last row

        today = date.today().strftime("%Y-%m-%d")

        if liszt == today:
            print(f'Abort: Data has already been collected for {today} :)')
            exit()
        else:
            print(f'Collecting current hit streak data for {today}... :)')