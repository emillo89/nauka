import collections
c1 = collections.Counter([1, 2, 3, 4, 5])
c2 = collections.Counter([4, 5, 6, 7, 8])
# additional
print(c1+c2)
# substraction
print(c1-c2)

# intersection
print(c1&c2)
# union
print(c1 | c2)