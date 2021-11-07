#list comprehension
numbers = [1,2,3]
new_list = [n + 1
    for n in numbers
]

#String as List
name = "Angela"
letters_list = [
    letter
    for letter in name
]

#Range as list
range_list = [
    double * double
    for double in range(1,5)
]

#Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
long_names = [name.upper()
               for name in names
               if len(name) >5
]

print(long_names)