def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(1,3,6,8))