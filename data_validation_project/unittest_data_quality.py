import unittest
import pandas as pd
from load_sample_data import read_data, load_config

class TestDataQuality(unittest.TestCase):

    def setUp(self):
        # Setup - Load the sample data (you can load your actual DataFrame here)
        self.df = read_data()
        self.expected_dtypes = load_config()['dtypes']
        
    #Test for dtypes
    def test_column_dtypes(self):
        """Test if DataFrame columns have correct dtypes"""
        for column, expected_dtype in self.expected_dtypes.items():
            with self.subTest(column=column):
                self.assertEqual(str(self.df[column].dtype), expected_dtype)

    # Test for duplicate rows
    def test_duplicates(self):
        """ Checking if there are any duplicate rows based on specific columns"""
        duplicates = self.df.duplicated(subset=['scheduled_day','appointment_day','patient_id', 'appointment_id'])
        self.assertFalse(duplicates.any(), "There are duplicate entries based on 'scheduled_day','appointment_day','patient_id' and 'appointment_id'.")

    # Test for missing values
    def test_missing_values(self):
        """Check if there are any missing values in the DataFrame"""
        missing = self.df.isnull().sum().sum()
        self.assertEqual(missing, 0, f"There are {missing} missing values in the DataFrame.")

    # Test for missing values in a specific column
    def test_missing_values_in_column(self):
        """Check if there are missing values in the scheduled_day','appointment_day','patient_id' and 'appointment_id' columns"""
        for column in ['scheduled_day','appointment_day','patient_id', 'appointment_id']:
            missing = self.df[column].isnull().sum()
            self.assertEqual(missing, 0, f"There should be 0 missing value in {column}, found {missing}.")

if __name__ == '__main__':
    unittest.main()