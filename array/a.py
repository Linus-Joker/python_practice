# 在 python 應該叫 list
import unittest
list = []


class Arr():
    # append結尾
    def add(self, list):
        # print(list[0:1])
        list.append('apple')
        return list

    # split
    def split(self, birStr):
        return birStr.split('/')

    # extend結合串列
    def extend(self, list):
        other = ['cat', 'dog']
        list.extend(other)
        print(list)

    # insert 加入項目
    def insert(self, list):
        list.insert(3, 'fish')
        print(list)

    # del 刪除項目
    def delete(self, list):
        del list[0]
        print(list)

    # pop 位移值取得項目並刪除
    def pop(self, list):
        list.pop(1)
        print(list)

    # index 尋找某個項目的位移值
    def index(self, list):
        print(list.index('apple'))

    # in 檢查是否存在某個值
    def check(self, list):
        print('apple' in list)
        print('sd4f5d' in list)

    # join()轉換字串
    def join(self, list):
        print(', '.join(list))


# a = Arr()
# a.add(list)
# a.split()
# a.extend(list)
# a.insert(list)
# a.delete(list)
# a.pop(list)
# a.index(list)
# a.check(list)
# a.join(list)


class ArrTest(unittest.TestCase):
    def test_add(self):
        a = Arr()
        fruitList = a.add(list)
        resultList = ['apple']
        self.assertEqual(resultList, fruitList)

    def test_split(self):
        a = Arr()
        bir = '1/6/1955'
        testList = a.split(bir)
        resultList = ['1', '6', '1955']
        self.assertEqual(testList, resultList)


if __name__ == '__main__':
    unittest.main()
