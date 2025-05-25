import insights as i, pandas as pd

print('Choose one of the following: \n' \
'1) Collect data \n' \
'2) Get insights')

response = int(input())

if response == 1:
    # enter all collection functions
    print('hello')

if response == 2:
    print('What do you want to see? \n' \
    '1) Standings\n' \
    '2) Win pct ranked\n' \
    '3) Hit streak leaders')

    choice = int(input())

    if choice == 1:
        print('Standings:\n')
        i.standings()