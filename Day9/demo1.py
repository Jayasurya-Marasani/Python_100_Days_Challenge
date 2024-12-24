# Dictionaries

test_dict = {
    1 : "a",
    2 : "b",
    3 : "c",
    4 : "d",
    5 : "e",
    6 : "f",
    7 : "g",
    8 : "h",
    9 : "i",
    10 : "j"        
}
# Loop through dictionary
for i in test_dict:
    print(test_dict[i])

test_dict[11] = "k"

print(test_dict[11])

empty_dict = {}
empty_dict["1"] = "a"

print(empty_dict)

# Edit an item in dictionary

empty_dict["1"] = "z"
print(empty_dict)

# Nesting

capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}
# Nested list in dictionary
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"]     
}

# print Lille

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nesting with dictionary in dictionary

travel_log = {
    "France" : {
        "num_times_visited" : 8,
        "cities_visited" : ["Paris", "Lille", "Dijon"]
    },
    "Germany" : {
        "num_times_visited" : 12,
        "cities_visited" : ["Stuttgart", "Berlin"]
    }
}

# print Stuttgart
print(travel_log["Germany"]["cities_visited"][0])