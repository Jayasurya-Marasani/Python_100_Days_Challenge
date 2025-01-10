import pandas as pd
import csv
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
    
#     print(temperatures)




df = pd.read_csv("weather_data.csv")
print(type(df))
print(type(df["temp"]))

data = df.to_dict()

print(data["temp"])

temp_list = df["temp"].to_list()
print(temp_list)

print(f"Avg : {sum(temp_list)/len(temp_list)}")

print(f"The DF avg is : {df["temp"].mean()}")

print(f"The DF mode is : {df["temp"].mode()}")

print(f"The DF median is : {df["temp"].median()}")

print(f"The Df max value is : {df['temp'].max()}")

# Get Data in columns

print(df.condition)

#get the row of the data using df

print(df[df.day == 'Monday'])

# print the row of data which had the highest temperature

print(df[df['temp']== df['temp'].max()])

monday = df[df['day']== 'Monday']
print(monday.condition)
print(monday['temp'])

c_temp = int(monday['temp'])

print(type(c_temp))
f_temp = (c_temp * (9/5)) + 32


print(f_temp)

# Create a df from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65],
}

df = pd.DataFrame(data_dict)

print(df.head())

df.to_csv("data.csv", index=False)

df = pd.read_csv("data.csv")

print(df.head())