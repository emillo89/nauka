class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print('How how')

class Cat(Animal):
    def voice(self):
        print('Moew moew')

class Wolf(Dog):
    def voice(self):
        print('jestem wilkiem')
        super().voice()

cat = Cat('kicius', 25)
print(cat.name,cat.age)
dog = Dog('Pikus',15)

wilk = Wolf('Wolf',15)
print(wilk.voice())