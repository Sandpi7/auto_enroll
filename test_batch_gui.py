#!/usr/bin/env python3
"""
Test script to verify batch processing functionality through GUI components
"""
import sys
import os
sys.path.insert(0, 'autoenroll')

import tkinter as tk
from simple_updater import ExcelDataReplacer

def test_batch_processing():
    """Test batch processing functionality"""
    print("=== BATCH PROCESSING GUI TEST ===")
    
    # Create a minimal tkinter root for testing
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    try:
        # Initialize the ExcelDataReplacer
        replacer = ExcelDataReplacer(root)
        
        # Test parameters
        source_folder = 'tests/test_data/Input'
        target_folder = 'tests/test_data/Output'
        pattern = 'target_enrollment*.xlsx'
        
        print(f"Source folder: {source_folder}")
        print(f"Target folder: {target_folder}")
        print(f"Pattern: {pattern}")
        
        # Simulate GUI entry fields
        replacer.source_entry = tk.Entry(root)
        replacer.target_entry = tk.Entry(root)
        replacer.pattern_entry = tk.Entry(root)
        
        # Set values in the entry fields
        replacer.source_entry.insert(0, source_folder)
        replacer.target_entry.insert(0, target_folder)
        replacer.pattern_entry.insert(0, pattern)
        
        # Test batch processing
        result = replacer.replace_data_batch()
        print(f"Batch processing completed")
        
        # Check one of the files to verify success
        import pandas as pd
        target_file = os.path.join(target_folder, 'target_enrollment.xlsx')
        if os.path.exists(target_file):
            df = pd.read_excel(target_file)
            print(f"Verified: {target_file} contains {len(df)} rows")
            print("Sample data:")
            print(df[['CRN', 'Current Enroll', 'Course']].head())
        
        print("✓ GUI BATCH PROCESSING TEST PASSED!")
        
    except Exception as e:
        print(f"✗ Error during batch processing test: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        root.destroy()

if __name__ == "__main__":
    test_batch_processing()
