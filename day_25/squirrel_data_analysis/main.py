# project: make the new file and find the squirrel count according to the color
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241226.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

color_count_dict = {
    "Primary Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Color Count" : [gray_count, black_count, cinnamon_count]
}

data = pandas.DataFrame(color_count_dict)
data.to_csv("squirrel_color_count.csv")
