import unittest

# 只要繼承TestCase 就可以使用setUp, tearDown 他們是unittest內附有的功能
class TestFucn(unittest.TestCase):
  # 測試前指令
  def setUp(self):
    print('start')

  #測試用(名稱要以test開頭)
  def test_func(self):
    print('test func')
    i = 1  
    self.assertEqual(i/1,1)
  
  def test_even(self):
    print('test_even')
    for i in range(6):
      with self.subTest(i=i):
        self.assertEqual(i % 2, 0)

  #測試完成後
  def tearDown(self):
    print('finish')


if __name__ == '__main__':
  unittest.main()