import unittest
from donor import *

a=blooddb("akas","asd","asf","ash","ght")
a.read_data(thelist)

class TestDonor(unittest.TestCase):
     def test_search_donor(self):
         result=blooddb.search_donor(self,"8553386870")
         expected="Found"
         self.assertEqual(expected,result)
         
     def test_search_donor1(self):
         result=blooddb.search_donor(self,"8553386890")
         expected="Not Found"
         self.assertEqual(expected,result) 

