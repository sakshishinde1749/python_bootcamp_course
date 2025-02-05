# for naming any file, class or function we use 3 representation
# 'PascalCase': mostly used for making class then we have 'camelCase' and 'snake_case'


class User:

    # init function is used to define some default attribute values rather than making every time, after creating any object 
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

        self.followers = 0  #default valued assigned
        self.following = 0

    # method making
    def follow(self, user):
        user.followers += 1
        self.following += 1

# making object from class user
user_1 = User("1", "ram02")
user_2 = User("2", "sham02")


user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)