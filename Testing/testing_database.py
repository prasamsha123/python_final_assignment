import unittest
from back_end.Connection import *

class test_search(unittest.TestCase):
    def setUp(self):
        self.dbconnect=DbConnection()

    def test_insert(self):
        query = 'insert into student values(%s,%s,%s,%s,%s,%s);'
        values= (111,'Naen','NaNv','39','Male','Japan')
        self.dbconnect.insert(query,values)
        expect=[(111,'Naen','NaNv','39','Male','Japan')]
        actual=self.dbconnect.select('select * from student where StudentID=111')
        self.assertEqual(expect,actual)

    def test_update(self):
        query = "update student set FirstName=%s,LastName=%s,Age=%s,Gender=%s,Address=%s where StudentID=%s;"
        values=('Sam','Bob','20','Male','Barcelona',1)
        self.dbconnect.update(query,values)
        expect=[(1,'Sam','Bob','20','Male','Barcelona')]
        actual=self.dbconnect.select('select * from student where StudentID=1')
        self.assertEqual(expect,actual)

    def test_delete(self):
        query='delete from student where StudentID=%s;'
        values=(0,)
        self.dbconnect.delete(query,values)
        expect = []
        actual = self.dbconnect.select('select * from student where StudentID=0')
        self.assertEqual(expect, actual)

if __name__=="__main__":
    unittest.main()




