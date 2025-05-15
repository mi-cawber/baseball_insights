import requests, bs4, csv, retrieval_functions as f


raw, list = f.retrieve_data('https://www.baseballmusings.com/cgi-bin/Standings.py?year=2025')

f.data_transfer(raw, list)

f.print_list(list)