def count_range_in_list(my_list,min,max):
    count=0
    for i in my_list:
        if min <= i <=max:
            count+=1

    return count

list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))