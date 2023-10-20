import unittest
import yaml
from sweep import Sweep

class TestSweep(unittest.TestCase):

    def setUp(self):
        with open('sweep.yaml', 'r') as file:
            self.sweep_config = yaml.safe_load(file)
        self.sweep = Sweep(self.sweep_config)

    def test_sweep_functionality1(self):
        # Arrange
        expected_result = 'expected_result1'
        
        # Act
        result = self.sweep.functionality1()
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_sweep_functionality2(self):
        # Arrange
        expected_result = 'expected_result2'
        
        # Act
        result = self.sweep.functionality2()
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_sweep_functionality3(self):
        # Arrange
        expected_result = 'expected_result3'
        
        # Act
        result = self.sweep.functionality3()
        
        # Assert
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
