import day as day


class Person():
    nums_of_person = 0
    raise_amount = 1.06

    def __init__(self,name, surname,pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = self.name + '.' + self.surname + '@wp.pl'

        Person.nums_of_person += 1

    def full_name(self):
        return '{} {}'.format(self.name,self.surname)

    def apply_amound(self):
        self.pay = int(self.pay * self.raise_amount)
    '''metoda class method'''
    @classmethod
    def set_raise_amound(cls,amound):
        cls.raise_amount = amound

    '''1. praktyczny przyklad zastosowania metody class'''
    @classmethod
    def from_string(cls,emp_str):
        name, surname,pay = emp_str.split('-')
        return cls(name,surname,pay)

    '''Zastosowanie metody statycznej'''
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    # 3. dunder method( za pomoca tego wyswietlimy obiektu, poszczegolne pola)
    def __repr__(self):
        return '{},{},{}'.format(self.name, self.surname, self.pay)
    def __str__(self):
        return '{} - {}'.format(self.full_name() ,self.email)
    # metoda __add__ i __len__
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())

osoba = Person('jarel','marek',5000)
osoba2 = Person('michal','jerzy',9000)

print(osoba.email)
print(osoba.pay)
osoba.apply_amound()
print(osoba.pay)
print(osoba.raise_amount)
osoba.raise_amount=1.1
print(osoba.__dict__)
print(Person.nums_of_person)

print('-----')
Person.set_raise_amound(1.30)
print(Person.raise_amount)

#zastooswanie metody class
osoba.set_raise_amound(1.40)
print(osoba.raise_amount)

'''Ad.1'''
emp_str_1 = 'John-Doe-7000'
emp_str_2 = ' Steve-Smith-30000'
emp_str_3 = ' Jane-Smoth-38000'

# name,surname,pay = emp_str_1.split('-')
# new_emp_1 = Person(name,surname,pay)
# print(new_emp_1.email)
# print(new_emp_1.pay)

'''taka zadanie byloby pracochlonne dlatego, użyjemy do tego metody class'''
print('------')

new_emp_1 = Person.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

'''Ad2 Zastowoanie metody statycznej'''

import datetime

my_date = datetime.date(2017,12,28)
print(Person.is_workday(my_date))

print(osoba.is_workday(my_date))


class Developer(Person):
    raise_amount = 1.3

    def __init__(self,name, surname,pay,prog_lang):
        super().__init__(name,surname,pay)
        self.prog_lang = prog_lang

dev = Developer('al','bundy',1000,'Java')
print(dev.email)
dev.apply_amound()
print(dev.pay)
print(dev.prog_lang)

dev2 = Developer('Max','Jakis',40000,'Python')

class Menager(Person):

    def __init__(self,name,surname,pay,employees = None):
        super().__init__(name,surname,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.full_name())



mgr_1 = Menager('Jack','Sparov',9000,[dev2])
print('++++++')
print(mgr_1.print_emps())
mgr_1.add_emp(dev)
print(mgr_1.__dict__)
print(mgr_1.print_emps())


# Ad.3 dunder methods

print(osoba.__repr__())
print(osoba.__str__())

# Ad.4 methoda __add__ i __len__
print(osoba.__add__(osoba2))
print(len(osoba))


