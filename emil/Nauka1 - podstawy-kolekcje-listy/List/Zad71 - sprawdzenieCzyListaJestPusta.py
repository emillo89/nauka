my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]

print(all(not i for i in my_list))
print(all(not i for i in my_list1))

for i in my_list1:
    print(i)