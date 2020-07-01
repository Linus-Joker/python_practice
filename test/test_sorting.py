import unittest


class TestSort(unittest.TestCase):
    # 測試前指令
    def setUp(self):
        print('start')

    # 測試用(名稱要以test開頭)
    def test_sort(self):
        y = [12, 11, 10]
        n = len(y)
        for i in range(len(y)):
            min_idx = y[i]
            print(i)
            for j in range(i, n, 1):
                # print(j, y[j])
                print(j)
                if y[j] < min_idx:
                    # min_idx = y[j]
                    y[i], y[j] = y[j], y[i]

    # 測試完成後
    def tearDown(self):
        print('finish')


if __name__ == '__main__':
    unittest.main()
