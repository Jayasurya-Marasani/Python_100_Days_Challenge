# File Not Found Error

# with open("daata.txt") as file:
#     file.read()


# KeyError

# a_dictionary = {"key" : "value"}
# a_dictionary["non_existent_key"]

# Index Error

# fruits = ["Apple", "Banana", "Pear"]
# fruit = fruits[3]

# Type Error
# text = "abc"
# print(text + 5)

#  we can use catch the Exceptions using try, except, else and finally

try:

    file = open("a_file.txt")
    a_dict = {"Key": "value"}
    # print(a_dict["asdf"])
    print(a_dict["Key"])

except FileNotFoundError:
    print("There was an error")
    file = open("a_file.txt", 'w')
    file.write("Something")

except KeyError as error_message:
    print(f"That key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    # file.close()
    # print("File was closed")
    raise KeyError("The message is that i made up")