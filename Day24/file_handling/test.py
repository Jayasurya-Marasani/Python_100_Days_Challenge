# Reading the File


with open("test.txt") as file:
    contents = file.read()
    print(contents)



# appends into the file

with open("test.txt", mode="a") as file:
    file.write("\nHello World") #adds to the text
