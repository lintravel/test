import unittest
@unittest.skip("pass")
class TestCaseDemo1(unittest.TestCase):

    def test_01_equal(self):
        a=1
        b=2
        self.assertEqual(a,b,"a和b不相等")
        self.assertNotEqual(a,b)

    def test_02_equal(self):
        a=1
        self.assertTrue(a)
        self.assertFalse(False)

    def test_03_equal(self):
        a=1
        B=2
        self.assertIs(a,B)
        self.assertIsNot(a,B)
        '''
        self.assertIsNone
        self.assertIsNotNone
        self.assertIn
        self.assertNotIn
        self.assertIsInstance
        self.assertNotIsInstance
        '''
if __name__=="__main__":
    unittest.main()