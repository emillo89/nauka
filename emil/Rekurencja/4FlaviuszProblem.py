'''4 (Problem Flawiusza). Załóżmy, że mamy n ludzi ponumerowanych od 1 do n ustawionych
w kręgu. „Eliminować” będziemy co drugą osobę, aż pozostanie tylko jeden człowiek. Nasz
problem polega na wyliczeniu przeżywającego numeru J(n), czyli znalezieniu wzoru ogólnego
lub rekurencyjnego dla funkcji J. Napisz program, który zwraca stosowną wartość (istnieje dość
proste rozwiązanie rekurencyjne, ale trzeba na nie wpaść).
1
Np. dla n = 10 porządek eliminowania jest następujący
2, 4, 6, 8, 10, 3, 7, 1, 9,
tak więc J(10) = 5'''

def josephus(n,k):
    if n == 1:
        return 1
    else:
        return (josephus(n-1,k) + k - 1) % n+1



print(josephus(10,2))

