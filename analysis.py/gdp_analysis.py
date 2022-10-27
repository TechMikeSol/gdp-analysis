import csv

def get_highest_gdp(data, year):
    # data is a list of dictionaries 
    # year is the object were searching through
    # data[0] is our dictionary
    # data[0][year] is the value
    # we will have as many k:v for as many columns
    # we will have as many dictionaries for as many rows we have
    # data[0][year] will return the value passed in
    # because we are key:value accessing
        maximum = float(data[0][year])
        state = ""
        for row in data:
            value = float(row[year])
            if value < maximum:
                continue
            maximum = value
            # if you only want the highest numeric GDP remove state = ""
            # and remove state = row["GeoName"]
            state = row["GeoName"]
        return state
        

def get_lowest_gdp(data, year):
        minimum = float(data[0][year])
        state = ""
        for row in data:
            value = float(row[year])
            if value < minimum:
                minimum = value
                state = row["GeoName"]
        return state

def get_state_gdp(data, state, year):
        for row in data:
            value = row["GeoName"]
            if state == value:
                return row[year]

# save each row into a list 
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
# load in data as DictReader, 
# dictreader gives one large dictionary of dictionaries & reads through all rows
# Keys are the values of the rows
# The reader object is an interable object
    reader = csv.DictReader(infile)
# go through each year and get highest and lowest gdp
    for row in reader:
            list_data.append(row)
            

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
# list_data object is a count of rows
maxgdp = (get_highest_gdp(list_data, '2020')) 
   
# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
lowestgdp = (get_lowest_gdp(list_data, '2020'))

stategdp = (get_state_gdp(list_data, 'Georgia', '2020'))

print('Highest GDP is:', maxgdp)
print('Lowest GDP is:', lowestgdp)
print('State GDP for Georgia is:', stategdp)