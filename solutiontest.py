import unittest
from testtdd import solution
class TestSolution(unittest.Testcase):
def test_addition(self):
	self.assertTrue(Solution(10,20,"+"),30)
def test_multiplication(self):
    self.assertTrue(Solution(10,20,"*"),200)
def test_division(self):
    self.assertTrue(Solution(10,20,"/"),0.5)
    
if __name__==" __main__":
	unittest.main()