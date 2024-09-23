"""args demo"""
def add(*args):
    """Sum the args passed in"""
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3, 4, 5))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)
print(my_car.model)
