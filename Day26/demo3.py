import pandas as pd

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

df = pd.DataFrame(student_dict)

print(df)
# Loop Through a data frame

print("\n\n")
for (key, value) in df.items():
    print(value)


# loop through rows of a data frame using iterrows

# Data Frame comprehension

# {new_key : new_value for (index, row) in df.iterrows()}

print("\n\n")

for (index, row) in df.iterrows():
    # print(row)
    # print(f"{row.student} with {row.score} marks")
    print(f"{row['student']} with {row['score']} marks")