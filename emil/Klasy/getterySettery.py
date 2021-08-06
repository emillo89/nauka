class Konto_bankowe():
    __stan = 0

    @property
    def stan_konta(self):
        return self.__stan

    @stan_konta.getter
    def stan_konta(self):
        return 'stan konta '+ str(self.__stan) + ' zl'

    @stan_konta.setter
    def stan_konta(self,value):
        self.__stan += value

konto = Konto_bankowe()
konto.stan_konta = 100
print(konto.stan_konta)
konto.stan_konta = 150
print(konto.stan_konta)
konto.stan_konta = -200
print(konto.stan_konta)