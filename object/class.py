from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def voice(self):
        pass


class Dog(Pet):
    def voice(self):
        print('%s: wjwjwjw' % self.name)


class Cat(Pet):
    def voice(self):
        print('%s: meow' % self.name)


dd = Dog('yellow')
dd.voice()

me = Cat('white')
me.voice()
