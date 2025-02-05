import pandas

data = pandas.read_csv("weather_data.csv")

# print whole table data
print(data)

# print any column of data
print(data["temp"]) 
print(data.temp)

# print any row of data
print(data[data.day == "Monday"])

# there are 2 types of data exists, Series(any list of data) and DataFrame(2D data)

print(type(data["temp"]))
print(type(data))

# pandas can convert data into dictionary
print(data.to_dict())

# pandas can convert series into list
print(data["temp"].to_list())

# avg of any list in pandas
print(data["temp"].mean())

# max in list temp
print(data["temp"].max())

