"""
PascalCase - class
camelCase
snake_case - everythink else
"""

class User():
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username




user_1 = User('1212','Emil ')
user_2 = User('1213', 'Jakis')
print(user_1.id)


