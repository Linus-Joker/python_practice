import unittest


class Person:  # 要測試的class
    def __init__(self, name):
        self.name = name
        self.age = 10

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age


class TestPerson(unittest.TestCase):
    def setUp(self):  # 每個測試初始化
        print('init')
        self.p = Person('John')

    def test_getName(self):  # 要測試的功能, 名稱需test開頭
        print('test getNme'),
        self.assertEqual(self.p.getName(), 'John')

    def test_setAge(self):
        print('test setAge'),
        self.assertEqual(self.p.age, 10)
        self.p.setAge(18)
        self.assertNotEqual(self.p.age, 10)

    def tearDown(self):  # 每個測試結束
        print('final')


if __name__ == '__main__':
    unittest.main()
