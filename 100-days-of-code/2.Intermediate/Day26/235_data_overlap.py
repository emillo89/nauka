with open("file1.txt", mode="r") as file:
    list_1 = file.readlines()

with open("file2.txt", mode="r") as file:
    list_2 = file.readlines()

new_list = [ int(num) for num in list_1 if num in list_2 ]
print(new_list)