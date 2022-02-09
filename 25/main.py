import csv

# with open("./25/weather_data.csv", mode='r') as weather_file:
#     data = csv.reader(weather_file)
#     next(data)
#     temperatures = []
#     for row in data:
#        temperatures.append(int(row[1]))
    # print(temperatures)

import pandas
# data = pandas.read_csv("./25/weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(sum(temp_list)/len(temp_list))

# average = data["temp"].mean()
# print(average)

# max = data["temp"].max()
# print(max)

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((int(monday.temp) * 1.8) + 32)

data = pandas.read_csv("./25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"]=="Gray"])
red = len(data[data["Primary Fur Color"]=="Cinnamon"])
black = len(data[data["Primary Fur Color"]=="Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray,red,black]
}
df = pandas.DataFrame(data_dict)
df.to_csv("./25/squirrel_count.csv")