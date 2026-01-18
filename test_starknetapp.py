# test_starknetapp.py
"""
Tests for StarknetApp module.
"""

import unittest
from starknetapp import StarknetApp

class TestStarknetApp(unittest.TestCase):
    """Test cases for StarknetApp class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StarknetApp()
        self.assertIsInstance(instance, StarknetApp)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StarknetApp()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
