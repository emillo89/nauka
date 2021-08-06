def max_element(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

print(max_element([10000,-10,12,1000]))

