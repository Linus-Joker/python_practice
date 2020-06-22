# 物件的繼承與複寫


class Person():
    def __init__(self, name):
        self.name = name


class Car():
    def make(self):
        print('I am a car!!')


class Yo(Car):
    def make(self):
        print('I am yo car!!')


# give_new_car = Car()
# give_new_yo = Yo()
# give_new_car.make()
# give_new_yo.make()
print(Car.make('car'))
