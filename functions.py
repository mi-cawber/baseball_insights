from datetime import date

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
        file.write(f'{today}')