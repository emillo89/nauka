def histogram(items):
    for n in items:
        output = ''
        while n>0:
            output+='*'
            n = n-1
        print(output)

histogram([2, 3, 6, 5])