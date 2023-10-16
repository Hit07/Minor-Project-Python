# with open("weather_data.csv") as data:
#     print(data.readlines())
import csv
import pandas
import pandas as pd
# -------------------------------------------------
# with open("weather_data.csv") as text:
#     data = csv.reader(text)
#     temp = []
#     for row in data:
#         # print(row)
#         if row[1].isdigit():
#             temp1 = row[1]
#             temp.append(int(temp1))
#     print(temp)
#--------------------------------------------------------

# data = pandas.read_csv("weather_data.csv")
'''For fetching values from column'''
# temp_list = data["temp"].to_list()
# sum_list = data["temp"].sum()
# avg_sum = round(sum_list/len(temp_list),4)
# print(avg_sum)
# max_value = data["temp"].max()
# print(max_value)
# print(data.condition)
'''For fetching values from row'''
# max_value = data.temp.max()
# print(data[data.temp == max_value])
# mon = data[data.day == "Monday"]
# print(f"{(mon.temp*1.8)+32}")
'''Creating dataframe from scratch'''
# data_dict = {
#     "students":["Any","James","Angela","Hitesh"],
#     "scores":[76,89,92,99]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("data_dict.csv")

# -------------------------------------------------------------------

squirrel_data = pd.read_csv("squirrel_data.csv")
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
color_data = {
    "Fur_color":["Gray", "Red", "Black"],
    "Count":[gray_count, cinnamon_count, black_count]
}
data = pd.DataFrame(color_data)
data.to_csv("Fur Color.csv")

# print(data)

# new_data = pd.read_csv("Fur Color.csv")
# print(new_data)
