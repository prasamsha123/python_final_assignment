import unittest
from front_end.add import *
class test_sort(unittest.TestCase):
    def setUp(self):
        self.c1 = [1,'Maths','Loral','2000','9/1/2021','12/1/2020']
        self.c2 = [111,'Networking','Eva','9/1/2020','10/1/2020']
        self.data = [self.c1, self.c2]
    def test_sort_descending(self):
        expect = [[111,'Networking','Eva','9/1/2020','10/1/2020'],[1,'Maths','Loral','2000','9/1/2021','12/1/2020']]
        actual = add_details.mergesort(self.data, False)
        self.assertEqual(actual, expect)

if __name__=="__main__":
    unittest.main()