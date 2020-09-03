import unittest
from front_end.add import *
class test_search(unittest.TestCase):
    def setUp(self):
        c1 = [1,'Maths','Loral','2000','9/1/2021','12/1/2020']
        c2 = [111,'Networking','Eva','9/1/2020','10/1/2020']
        self.value = [c1, c2]
    def test_search(self):
        search_value = 'Maths'
        index = 1
        expect = [[1,'Maths','Loral','2000','9/1/2021','12/1/2020']]
        actual = add_details.search(self.value, search_value, index)
        self.assertEqual(actual, expect)

if __name__=="__main__":
    unittest.main()

