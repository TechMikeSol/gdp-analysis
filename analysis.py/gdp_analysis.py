import csv

def get_highest_gdp(data, year):
    maximum = float(data[0][year])
    for row in data:
        value = float(row[year])
        if value > maximum:
            maximum = value
    return maximum
    

def get_lowest_gdp(data, year):
    minimum = float(data[0][year])
    for row in data:
        value = float(row[year])
        if value < minimum:
            minimum = value
    return minimum

# save each row into a list 
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
print(reader.get_highest_gdp(""))

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"

