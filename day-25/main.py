# import csv
#
# with open("./weather_data.csv") as data_file:
#     # data = data_file.readlines()
#     # print(data)
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
