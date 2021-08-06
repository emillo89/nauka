a = [10,20,30,20,10,50,60,40,80,50,40]
newA = []
def remove_duplication(list):
    for i in list:
        if i not in newA:
            newA.append(i)
    return newA

print(remove_duplication(a))

# dla zbioru
zbior = set()
def remove_duplication_set(list):
    for i in list:
        zbior.add(i)
    return zbior

print(remove_duplication_set(a))
