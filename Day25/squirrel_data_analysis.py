import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(df.columns)
black_num = len(df[df['Primary Fur Color'] == 'Black'])

gray_num = len(df[df['Primary Fur Color'] == 'Gray'])

cinnamon_num = len(df[df['Primary Fur Color'] == 'Cinnamon'])


data = {
    "Fur" : ["Gray", "Black", "Cinnamon" ],
    "Count" : [gray_num, black_num, cinnamon_num]

}

df_analysed = pd.DataFrame(data)
df_analysed = df_analysed.rename_axis(("Index"))

print(df_analysed.head())

df_analysed.to_csv("squirrel_analyzed_data.csv", index = True)

# fur_color_counts = df["Primary Fur Color"].value_counts()

# print(fur_color_counts)