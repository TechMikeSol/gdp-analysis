#### gdp-analysis

GDP is important because it gives information about the size of the economy and how an economy is performing. 

In analysis.py you will find gdp_analysis.py which contains the code for the analysis.

`def get_highest_gdp(data, year):`  

This function will return the name of the state had the highest GDP for a specified year. It takes in a string `year` as an argument. `data` will be a `DictReader` object containing data.  

`def get_lowest_gdp(data, year):`  

This function will return the name of the state had the lowest GDP for a specified year. It takes in a string `year` as an argument. `data` will be a `DictReader` object containing data.  

`def get_state_gdp(data, state, year):`  

This function will return gdp value of some specific state for some specific year column. The name of the state will be passed in `state`, and the year will be passed in via `year.
