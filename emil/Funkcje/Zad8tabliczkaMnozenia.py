"""8) Wygeneruj na ekranie tabliczke mnozenia 10 x 10."""
# 1 sposob
for i in range(1,11):
    for j in range(1,11):
        print(i, ' x ',j, '=',i*j)

# 2 sposob
print(60*"-")
for y in range(1,11):
     for x in range(1,11):
          print (f" {x*y:>3} ", end="|")
     print()
     print(60*"-")

wycentrowany = 12
do_prawej = 55
do_lewej = 23

print(f"|{wycentrowany:^12}|{do_prawej:>15}|{do_lewej:<5}|")