import retrieval as r

raw, list = r.retrieve_data('https://www.baseball-reference.com/leagues/majors/2025-standard-batting.shtml#players_standard_batting')

r.data_transfer2(raw, list)

print(list)




                

