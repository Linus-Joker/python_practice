car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
# print(car)

# update() 沒有就新增，有就覆蓋
# car.update({'color': 'White'})
# print(car)

# get() 得到指定鍵值，沒有返回None
# print("model: ", car.get('model'))

# clear() 刪除字典所所有元素
# print(car)
# print(car.clear())

# dict.values() 返回一個迭代器，
# 可以使用 list() 来轉換為列表，列表為字典中的所有值
# print("car dict all value:", list(car.values()))

# pop() 方法删除字典给定键 key 所對應的值，返回值為被删除的值。
# key值必须给出。 否則，返回default值
print(car.pop('year'))
