# import csv  # python 内置了csv库作为标准库
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)  # 打印的是data这个对象的内存地址
#
#     temperatures = []  # 创建一个用来存储temperate的空列表
#     for row in data:
#         if row[1] != "temp":  # 去飚label
#             temperatures.append(row[1])
#     print(temperatures)  # ['12', '14', '15', '14', '21', '22', '24']

# 开始使用pandas
# import pandas as pd  # 导入pandas并且命名为pd
#
# data = pd.read_csv("weather_data.csv")  # 使用pandas的read_csv来导入weather_data.csv文件
# print(data)  # 打印整个数据
#
# print()
#
# print(data["temp"])  # 打印 label 为 temp 的列的数据
#
# print()
#
# # 我们可以来看一下我们获得的数据类型是怎么样的
# print(type(data))  # 结果为 DataFrame
#
# print()
#
# # 那要只是一列呢？
# print(type(data["temp"]))  # 结果为 Series
#
# print()
#
# data_dict = data.to_dict()  # 通过to_dict()可以将其转换为字典格式
# print(data_dict)
#
# print()
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# # 或者我们可以使用pandas提供的各种方法
# print(data["temp"].mean())  # mean()可以求取平均数
# print(data["temp"].max())  # max()可以求取最大值
#
# # get data in columns
# print(data["condition"])
# print(data.condition)  # data . condition可以调出data对象种的condition部分
#
# print()
#
# # get row in data
# print(data[data.day == "Monday"])
#
# print()
# print(data[data.temp == data.temp.max()])  # temp最大的情况
#
# print()
#
# # 让我们来查看monday
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print()
#
# # monday的温度转换为摄氏度
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

import pandas as pd

data = pd.read_csv("Central_Park_Squirrel_Census_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

# 将Dictionary 转换为 DataFrame
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")  # 然后本地多出了一个csv文件