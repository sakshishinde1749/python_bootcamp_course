import pandas

data = pandas.read_csv("weather_data.csv")

monday = data[data.day == "Monday"]
print(monday.condition)

# monday temp in fahrenheit
print((monday.temp[0] * 9/5) + 32)

# create dataframe from scratch
data_dict = {
    "students" : ["amy", "sakshi", "chinu", "shubhu"],
    "scores" : [90, 80, 90, 97]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


