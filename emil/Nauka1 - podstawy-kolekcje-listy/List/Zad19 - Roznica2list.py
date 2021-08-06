# 1 sposob aby sprawdzic roznice list
from collections import Counter

list1 = [1,2,3,4,5]
list2 = [2,3,4]
print(set(list1)-set(list2))

# 2 sposob na sprawdzenie roznicy list

color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

Counter1 = Counter(color1)
Counter2 = Counter(color2)
print(list(Counter1-Counter2)) ;"""wyswietli nam tylko co jest roznica"""
print(Counter1-Counter2) ; """wyswietli nam co jest roznica i ile ilosciowo jest tego czyli np red : 1"""