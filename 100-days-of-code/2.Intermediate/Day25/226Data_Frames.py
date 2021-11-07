import pandas

data = pandas.read_csv("weather_data.csv")

# #convert DATA FRAME to the dict
# data_dict = data.to_dict()
# print(data_dict)
#
# #convert SIRIES to the list
# temp_list = data["temp"].to_list()
#
# # average temperatures
# average = data["temp"].mean()
# print(average)
#
# #max temperature
# max_temp = data["temp"].max()
# print(max_temp)
#
# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 1.8 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

'#convert data to csv'
data.to_csv("new_data.csv")
