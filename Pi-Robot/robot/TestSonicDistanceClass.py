import unittest
from SonicDistance import SonicDistanceClass

class TestDistance(unittest.TestCase):
    sd = SonicDistanceClass()
    
    def test_GetDistance(self):
        d = sd.GetDistance()
        self.assertAlmostEqual(d, 10.0, 2, 'Incorrect distance??')
        
    def test_AtDistance(self):
        self.assertTrue(sd.AtDistance(10), 'Object at 10??')
        