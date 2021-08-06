from collections import Counter

s = 'lkseropewdssafsdfafkpwe'

print('Orginalny tekst: ',s)
# wskzanie ile jaki jest znak pod danym indexem i ile go jest
print(Counter(s).most_common(1))

# za pomoca petli wskazemy ile dany znak zostal powtorzony:
for i in Counter(s).most_common():
    print(i)

