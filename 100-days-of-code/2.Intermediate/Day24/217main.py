# with open("217my_file.txt") as file:
#     contents = file.read()
#     print(contents)


with open("217my_file.txt", mode= "a") as file:
    file.write("new text")