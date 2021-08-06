# sortowanie po pierwszej liczbie
def sort_list(tuples):
    return sorted(tuples)

print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# sortowanie po drugiej liczbie w tupli
def last(n):
    return n[-1]
print(last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),(1,3)]))

def sort_list(tuples):
    return sorted(tuples,key=last)

print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1),(1,3)]))


def sort(list):
    return list[list-1]