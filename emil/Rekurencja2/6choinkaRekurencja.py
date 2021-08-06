'''6. Podaj rekurencyjna definicje funkcji void piramida(int level); której
zadaniem jest narysowanie na ekranie nastepujacej piramidy:
*****
****
***
**
*'''

def choinka(n):
    if n <= 1:
        return '*'
    else:
        return n*"*" +'\n' + choinka(n-1)

print(choinka(5))