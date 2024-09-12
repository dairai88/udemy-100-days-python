"""main"""
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240910.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

fur_data_frame = pandas.DataFrame.from_dict(data_dict)
print(fur_data_frame)
fur_data_frame.to_csv("squirrel_count.csv", index=False)