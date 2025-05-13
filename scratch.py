
# transfers Tag data into array
def data_transfer(raw, array):
    # we don't want these items in the array
    blacklist = ['Player', 'Games', 'At Bats', 'Runs', 'Hits',
                 'HR', 'RBI', 'BB', 'K', 'BA', 'OBA', 'Slug%',
                 'Last Game Date', '']
    for element in raw:
        # if the element is a member of the blacklist, skip
        if element.getText() in blacklist:
            continue
        # if okay, add to array
        else:
            array.append(element.getText())

# shows data array
def print_array(array):
    # show length
    print(f'The length of the array is: {len(array)}', '\n')
    for element in array:
        print(element)


def array_csv(array, csv):
    # open file
    with open(csv, 'a') as file:
        for element in array:
            file.write(f'{element},')
