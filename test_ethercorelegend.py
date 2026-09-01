# test_ethercorelegend.py
"""
Tests for EtherCoreLegend module.
"""

import unittest
from ethercorelegend import EtherCoreLegend

class TestEtherCoreLegend(unittest.TestCase):
    """Test cases for EtherCoreLegend class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherCoreLegend()
        self.assertIsInstance(instance, EtherCoreLegend)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherCoreLegend()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
