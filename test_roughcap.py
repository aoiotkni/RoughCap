# test_roughcap.py
"""
Tests for RoughCap module.
"""

import unittest
from roughcap import RoughCap

class TestRoughCap(unittest.TestCase):
    """Test cases for RoughCap class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughCap()
        self.assertIsInstance(instance, RoughCap)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughCap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
