import unittest
from model.Library import *

class test_Library(unittest.TestCase):
    def setUp(self):
        self.d = Library(1,'CRUX','Jacob','Student','William','Bob','2077-02-22','Croatia')

    def test_get_ID(self):
        self.assertEqual(1, self.d.get_BookID())

    def test_get_BookTitle(self):
        self.assertEqual('CRUX', self.d.get_BookTitle())

if __name__=="__main__":
    unittest.main()

