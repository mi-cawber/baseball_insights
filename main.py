'''
Main module, for running retrieval functions.
'''
import retrieval as r, insights as i

# controls flow
switch = False

while not switch:
    # main prompt
    print('Choose one of the following: \n' \
    '1) Collect data \n' \
    '2) Get insights')

    response = int(input())

    # collect data
    if response == 1:
        
        # to collect hit streak data
        r.date_checker('hit_streaks_2025.csv', 'hit streak')
        raw, list = r.retrieve_data('https://www.baseballmusings.com/cgi-bin/CurStreak.py')
        r.data_transfer(raw, list) # transfers Tag data to list
        r.list_csv(list,'hit_streaks_2025.csv') # import into csv file

        # to collect standings data
        r.date_checker('standings_2025.csv', 'standings')
        raw, list = r.retrieve_data('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025')
        r.data_transfer(raw, list)
        r.list_csv(list,'standings_2025.csv')

        print('Success!')

        switch = True

    # insights menu
    if response == 2:
        print('What do you want to see? \n' \
        '1) Standings\n' \
        '2) Win pct ranked\n' \
        '3) Highest hit streaks')

        #capture user input
        choice = int(input())

        # print standings data
        if choice == 1:
            i.standings()
            switch = True

        # print win % data
        if choice == 2:
            i.win_pct()
            switch = True
        if choice == 3:
            i.highest_hit_streaks()
            switch = True
        else:
            print('Invalid input')