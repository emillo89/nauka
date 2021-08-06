class Person():
    nums_of_person = 0
    raise_amount = 1.06

    def __init__(self,name, surname):
        self.name = name
        self.surname = surname


        Person.nums_of_person += 1


    # 1. wlasciwosci
    @property
    def email(self):
        return '{}.{}@gmail.pl'.format(self.name,self.surname)
    @property
    def full_name(self):
        return '{} {}'.format(self.name,self.surname)

    @full_name.setter
    def full_name(self,imie):
        name,surname = imie.split(' ')
        self.name = name
        self.surname = surname

    @full_name.deleter
    def full_name(self):
        print('Delete Name!')
        self.name = None
        self.surname = None


osoba = Person('jarel','jak')
osoba.full_name = 'jakis Pan'
# osoba2 = Person('michal','jerzy')
#Ad.1 wlasciwosci
print(osoba.email)
print(osoba.full_name)
del osoba.full_name