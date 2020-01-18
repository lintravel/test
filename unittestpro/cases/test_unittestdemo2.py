import unittest
import selenium 

class TestCaseDemo2(unittest.TestCase):
    def test_01_sele(self):
        print("hello!")
    def test_02_add(self):
        a=1
        b=1
        self.assertEqual(a,b)
