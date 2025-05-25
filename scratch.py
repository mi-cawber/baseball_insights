import insights as i, pandas as pd

switch = False
while not switch:
    print('Choose one of the following: \n' \
    '1) Collect data \n' \
    '2) Get insights')

    response = int(input())

    if response == 1:
        # enter all collection functions
        print('hello')
        switch = True

    if response == 2:
        print('What do you want to see? \n' \
        '1) Standings\n' \
        '2) Win pct ranked\n' \
        '3) Highest hit streaks')

        choice = int(input())

        if choice == 1:
            i.standings()
            switch = True
        if choice == 2:
            i.win_pct()
            switch = True
        if choice == 3:
            i.highest_hit_streaks()
            switch = True
        else:
            print('Invalid input')