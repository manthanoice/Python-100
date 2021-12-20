def calculate(**kwargs):
    print(2)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make='Nissan', model='Ehe')
print(my_car.make)