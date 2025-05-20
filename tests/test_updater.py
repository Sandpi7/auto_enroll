import os
import sys
import unittest
import pandas as pd
import tkinter as tk

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from autoenroll.simple_updater import ExcelDataReplacer

class TestEnrollmentUpdater(unittest.TestCase):
    def setUp(self):
        """Create test data"""
        # Create source DataFrame
        self.source_data = {
            'CRN': ['12345', '67890', '11111'],
            'Actual': [25, 30, 15]
        }
        self.source_df = pd.DataFrame(self.source_data)
        
        # Create target DataFrame 
        self.target_data = {
            'CRN': ['12345', '67890', '11111', '22222'],
            'Current Enroll': [20, 28, 12, 18]
        }
        self.target_df = pd.DataFrame(self.target_data)
        
        # Save test files
        os.makedirs('tests/data', exist_ok=True)
        self.source_file = 'tests/data/source.xlsx'
        self.target_file = 'tests/data/target.xlsx'
        self.source_df.to_excel(self.source_file, index=False)
        self.target_df.to_excel(self.target_file, index=False)

    def tearDown(self):
        """Clean up test files"""
        if os.path.exists('tests/data'):
            for f in os.listdir('tests/data'):
                os.remove(os.path.join('tests/data', f))
            os.rmdir('tests/data')

    def test_update_enrollment(self):
        """Test that enrollments are updated correctly"""
        # Create a temporary root window
        root = tk.Tk()
        app = ExcelDataReplacer(root)
        
        # Set source and target files
        app.source_entry.insert(0, self.source_file)
        app.target_entry.insert(0, self.target_file)
        
        # Update enrollment data
        app.replace_data()
        
        # Read the updated target file
        updated_df = pd.read_excel(self.target_file)
        
        # Check updates were made correctly
        self.assertEqual(updated_df.loc[0, 'Current Enroll'], 25)  # Was 20
        self.assertEqual(updated_df.loc[1, 'Current Enroll'], 30)  # Was 28 
        self.assertEqual(updated_df.loc[2, 'Current Enroll'], 15)  # Was 12
        self.assertEqual(updated_df.loc[3, 'Current Enroll'], 18)  # Unchanged
        
        # Clean up
        root.destroy()

if __name__ == '__main__':
    unittest.main()
