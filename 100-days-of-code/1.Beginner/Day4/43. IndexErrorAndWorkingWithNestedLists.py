
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#index error
length = len(fruits)
print(length)
# we create index error
# print(fruits[length])
print(fruits[length-1])

#nested lists
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)