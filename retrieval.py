'''
The functions in this file concern the retrieval 
of baseball data from the internet and storing 
it into csv files.
'''
import requests, bs4, csv
from datetime import date

# big boss function, receives data
def scraping_pipeline(url, data_file, data_name):
    #this will first check to see if data is already current
    date_checker(data_file, data_name)

    # returns Response object
    res = requests.get(url)

    # returns BeautifulSoup object
    soup = bs4.BeautifulSoup(res.text, 'html.parser') 

    # returns Tag object
    raw = soup.select('td .number, td .letter') 

    # stores data
    list = [] # to store data
    return raw, list

# transforms Tag data into python list
def Tag_to_list(raw, list):
    # we don't want these items in the list
    # this data is captured from bs4 because of my soup.select() parameters
    blacklist = ['Player', 'Games', 'At Bats', 'Runs', 'Hits',
                 'HR', 'RBI', 'BB', 'K', 'BA', 'OBA', 'Slug%',
                 'Last Game Date', 'AL East', 'AL Central',
                 'AL West', 'NL East', 'NL Central', 'NL West',
                 'Record', 'Win Pct', 'Division GB', 'WildCard GB',
                 'League GB']
    for element in raw:
        # if the element is a member of the blacklist, skip
        if element.getText() in blacklist:
            continue
        # if data I want, then add to the list
        else:
            list.append(element.getText())
    # get rid of pesky '\n's in player strings
    for i in range(len(list)):
        list[i] = list[i].strip()

# this function is temporary (probably)
# 8/3/25.. I don't know what this is for
def data_transfer2(raw, list):
    # we don't want these items in the list
    for element in raw:
            list.append(element.getText())
    # get rid of pesky '\n's in player strings
    for i in range(len(list)):
        list[i] = list[i].strip()

# inserts data into csv
def list_to_csv(list, csv):
    # will be needed later
    today = date.today().strftime("%Y-%m-%d")
    # open file in append mode
    with open(csv, 'a') as file:
        # enumerate() gives index and value
        for index, element in enumerate(list):
            # if a player's name
            if element[0].isalpha():
                    # if first element of list
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
# file = the file that will be checked to see if data had already been collected on current day
# data = a simple placeholder for printing which dataset is current if necessary
def date_checker(file, data):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        liszt = list(reader)
        liszt = liszt[-1][-1] #last element of last row

        today = date.today().strftime("%Y-%m-%d")

        if liszt == today:
            print(f'Abort: {data} data has already been collected for {today} :)')
            exit() #This will just end the script
        else:
            print(f'Collecting {data} data for {today}... :)')
