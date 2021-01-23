car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}


class Car():

    def print(self, items):
        print(items)

    def get(self, items):
        # get() 得到指定鍵值，沒有返回None
        print("model: ", items.get('model'))

    def update(self, items):
        # update() 沒有就新增，有就覆蓋
        items.update({'color': 'White'})
        print(items)

    def value(self, items):
        # dict.values() 返回一個迭代器，
        # 可以使用 list() 来轉換為列表，列表為字典中的所有值
        print("car dict all value:", list(items.values()))

    def clear(self, items):
        # clear() 刪除字典所所有元素
        print(car)
        print(items.clear())

    def pop(self, items):
        # pop() 方法删除字典给定键 key 所對應的值，返回值為被删除的值。
        # key值必须给出。 否則，返回default值
        print(items.pop('year'))


c = Car()

# c.print(car)
# c.get(car)
# c.update(car)
# c.value(car)
# c.clear(car)
# c.pop(car)
