# 物件的繼承與複寫
# 物件繼承複寫後可以在子類使用並添加新方法
# 但是原本父類不能去調用子類寫的方法

# super呼叫父類別的方法


class Person():
    def __init__(self, name):
        self.name = name

# 當為類別定義__init__()方法，代表要用它來取代父類別的__init__()方法


class Car(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = Car('Bob', 'bob@mail.com')
print(bob.name, bob.email)
