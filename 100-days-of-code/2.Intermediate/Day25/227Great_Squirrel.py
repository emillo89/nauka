import pandas

data = pandas.read_csv("squirerl_count.csv")
# print(data["Primary Fur Color"])

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(data_dict)


new_data.to_csv("count_squirrels_data.csv")


