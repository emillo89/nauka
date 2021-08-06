def concatenate_list_data(list):
    ciag = ''
    for i in list:
        ciag = ciag +str(i)
    return ciag

print(concatenate_list_data([1, 5, 12, 2]))