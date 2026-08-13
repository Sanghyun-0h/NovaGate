# test_novagate.py
"""
Tests for NovaGate module.
"""

import unittest
from novagate import NovaGate

class TestNovaGate(unittest.TestCase):
    """Test cases for NovaGate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaGate()
        self.assertIsInstance(instance, NovaGate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaGate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
