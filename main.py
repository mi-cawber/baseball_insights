import functions as f

f.date_checker()
raw, array = f.retrieve_data()
f.data_transfer(raw, array) # transfers Tag data to array
f.array_csv(array,'data.csv') # import into csv file
