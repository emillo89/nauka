"""4)Napisz program wyznaczajacy najmniejsza liczbe podzielna przez 7,
która przy dzieleniu przez 2, 3, 4, 5, 6 daje reszte r = 1."""
for i in range(1,1000):
    if i%7 == 0 and i%2 == 1 and i%3 == 1 and i%4 == 1 and i%5 == 1 and i%6 ==1:
        print("najmniejsza liczba to: ",i)
        break
