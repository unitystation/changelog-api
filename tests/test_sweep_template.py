import unittest
from .github.ISSUE_TEMPLATE import sweep_template

class TestSweepTemplate(unittest.TestCase):

    def setUp(self):
        self.sweep_template = sweep_template.SweepTemplate()

    def test_sweep_template_functionality1(self):
        # Arrange
        expected_result = 'expected_result1'
        
        # Act
        result = self.sweep_template.functionality1()

        # Assert
        self.assertEqual(result, expected_result)

    def test_sweep_template_functionality2(self):
        # Arrange
        expected_result = 'expected_result2'
        
        # Act
        result = self.sweep_template.functionality2()

        # Assert
        self.assertEqual(result, expected_result)

    def test_sweep_template_functionality3(self):
        # Arrange
        expected_result = 'expected_result3'
        
        # Act
        result = self.sweep_template.functionality3()

        # Assert
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
