import functions as f

raw, array = f.retrieve_data()
f.data_transfer(raw, array) # transfers Tag data to array
f.array_csv(array,'test.csv') # import into csv file
