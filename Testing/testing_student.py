import unittest
from model.student import *

class test_student(unittest.TestCase):
    def setUp(self):
        self.d = Student(1,'William','Jacob','20','Male','Spain')

    def test_get_StudentID(self):
        self.assertEqual(1, self.d.get_StudentID())

    def test_get_Age(self):
        self.assertEqual('20', self.d.get_Age())

if __name__=="__main__":
    unittest.main()