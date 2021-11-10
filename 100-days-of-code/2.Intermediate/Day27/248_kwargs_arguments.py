def calculator(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculator(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", colour="red")
print(my_car.model)
print(my_car.colour)