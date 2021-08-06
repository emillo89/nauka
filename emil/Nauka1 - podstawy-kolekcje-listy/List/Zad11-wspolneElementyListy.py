# 1 sposob
def common_member(list1,list2):
    for i in list1:
        if i in list2:
            return True




print(common_member([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_member([1, 2, 3, 4, 5], [6, 7, 8, 9]))

# 2 sposob
def common_member(list1,list2):
    result = False
    for i in list1:
        for j in list2:
            if i == j:
                result=True
    return result

print(common_member([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_member([1, 2, 3, 4, 5], [6, 7, 8, 9]))
