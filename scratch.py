import retrieval_functions as f

f.date_checker('standings.csv')
raw, list = f.retrieve_data('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025')
f.data_transfer(raw, list)
f.list_csv(list,'standings.csv') 
