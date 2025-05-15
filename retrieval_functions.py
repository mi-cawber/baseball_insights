import requests, bs4, csv
from datetime import date

# big boss function, receives data
def retrieve_data(url):
    res = requests.get(url) #returns response object
    soup = bs4.BeautifulSoup(res.text, 'html.parser') # returns BeautifulSoup object
    raw = soup.select('td .number, td .letter') # captures data in Tag format
    list = [] # to store data
    return raw, list

# transfers Tag data into list
def data_transfer(raw, list):
    # we don't want these items in the list
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
        # if okay, add to list
        else:
            list.append(element.getText())
    # get rid of pesky '\n's in player strings
    for i in range(len(list)):
        list[i] = list[i].strip()

# shows data list
def print_list(list):
    # show length
    print(f'The length of the list is: {len(list)}', '\n')
    for element in list:
        print(element)

# inserts data into csv
def list_csv(list, csv):
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
def date_checker(file):
    with open(file, 'r') as file:
        reader = csv.reader(file)
        liszt = list(reader)
        liszt = liszt[-1][-1] #last element of last row

        today = date.today().strftime("%Y-%m-%d")

        if liszt == today:
            print(f'Abort: Data has already been collected for {today} :)')
            exit()
        else:
            print(f'Collecting data for {today}... :)')