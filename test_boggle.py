import unittest
from boggle import *

class TestBoggle(unittest.TestCase):
    
    def test_is_this_thing_on(self):
        self.assertTrue(check())
    
    