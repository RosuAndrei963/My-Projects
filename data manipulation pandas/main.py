# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# temperature = monday.temp[0]
# F_temp = temperature * 9/5 + 32
# print(F_temp)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")