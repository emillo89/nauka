#FileNotFound
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
#which key was the problem
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
#without except, execute this code
else:
    content = file.read()
    print(content)
#some code that's gonna run no matter what happens above
finally:
    file.close()
    print("File was closed")
#KeyError
# a_dictionary = {"key" : "value"}
# print(a_dictionary["new"])

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# print(fruit_list[3])

#TypeError
# text = "abc"
# print(text + 5)