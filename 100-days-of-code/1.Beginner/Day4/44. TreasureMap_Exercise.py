"""
Instructions
You are going to write a program which will mark a spot with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what the nested list looks like:
['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1][horizontal - 1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇

print(f"{row1}\n{row2}\n{row3}")
print('---')
# if you modify simple lists, you modify nested lists for example:
row1[1] = "55"
print(f"{row1}\n{row2}\n{row3}")
