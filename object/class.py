from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    # py 抽象練習
    def __init__(self, name):
        self.name = name

    def run(self):
        print('fast')

    @abstractmethod
    def voice(self):
        pass

    def eat(self):
        print('飼料')


class Dog(Pet):
    def voice(self):
        print('%s: wjwjwjw' % self.name)


class Cat(Pet):
    def voice(self):
        print('%s: meow' % self.name)


dd = Dog('yellow')
dd.voice()
dd.run()
dd.eat()

me = Cat('white')
me.voice()
me.eat()
