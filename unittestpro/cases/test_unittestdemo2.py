#unittest框架管理测试用例
import unittest 
#定义测试类以"Test"开头
#申明class继承unittest.TestCase方法
class TestCaseDemo2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("execute setUpClass")

    @classmethod
    def tearDownClass(self):
        print("execute tearDownClass")

    def setUp(self):
        print("execute setUp")

    def tearDown(self):
        print("execute tearDown")

    #所有测试方法以"test"开头
    def test_01_sele(self):
        print("hello!")
    def test_02_add(self):
        a=1
        b=1
        self.assertEqual(a,b)

if __name__ == "__main__":
    unittest.main()