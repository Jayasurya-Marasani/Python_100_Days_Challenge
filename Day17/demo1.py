# Creating Classes
# For Naming the Classes using PascalCase i.e use the first letter of every word as Capital without any spaces.
# camelCase is first word is lower case and remaining words are Upper Case
# snake_case is where all the words are seperated by underscore. These are mostly used in function names
class User:
    
    name = "class" 
    # Constructor
    def __init__(self, user_id = None, username = None):
        print("new user being created...")    
        self.id = user_id
        self.username = username 
        self.followers = 0
        self.following = 0 
    def get_name(self):
        return self.username + User.name
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
# user_1 = User()

# Working with Attributes

# user_1.id = "001"
# user_1.username = "Surya"

# print(user_1.username)

# Well these work with only for the user_1 object. If we create an new object then again we need to define those attributes. So we can directly define them in class User with the help of constructor(initializing an object)

user_1 = User("001", "Surya")
user_2 = User()
user_2.id = "002"
user_2.username = "Jaya"

print(f"User 1 : {user_1.id} and {user_1.username}")
print(f"User 2 : {user_2.id} and {user_2.username}")

print(user_2.get_name())

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)