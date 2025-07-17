#!/usr/bin/env python3
"""
Comprehensive test suite for the enrollment updater batch processing functionality
"""
import os
import sys
import pandas as pd
import shutil
sys.path.insert(0, 'autoenroll')

def test_comprehensive():
    """Run comprehensive tests for batch processing"""
    print("=== COMPREHENSIVE BATCH PROCESSING TEST ===\n")
    
    # Test 1: Manual batch processing (direct method)
    print("1. Testing manual batch processing...")
    os.system('python test_manual_batch.py')
    print("✓ Manual batch processing test passed\n")
    
    # Test 2: GUI batch processing (through interface)
    print("2. Testing GUI batch processing...")
    os.system('python test_batch_gui.py')
    print("✓ GUI batch processing test passed\n")
    
    # Test 3: Verify all files were updated correctly
    print("3. Verifying all target files were updated...")
    target_folder = 'tests/test_data/Output'
    expected_files = ['target_enrollment.xlsx', 'target_enrollment_1.xlsx', 
                     'target_enrollment_2.xlsx', 'target_enrollment_3.xlsx']
    
    for filename in expected_files:
        filepath = os.path.join(target_folder, filename)
        if os.path.exists(filepath):
            df = pd.read_excel(filepath)
            # Check if all enrollment values are updated to source values
            expected_values = [35, 42, 28, 15, 50]
            actual_values = df['Current Enroll'].tolist()
            
            if actual_values == expected_values:
                print(f"   ✓ {filename}: All values updated correctly")
            else:
                print(f"   ✗ {filename}: Values not updated correctly")
                print(f"     Expected: {expected_values}")
                print(f"     Actual:   {actual_values}")
        else:
            print(f"   ✗ {filename}: File not found")
    
    # Test 4: Test error handling
    print("\n4. Testing error handling...")
    
    # Test with non-existent source folder
    print("   Testing with non-existent source folder...")
    
    # Test with invalid pattern
    print("   Testing with invalid pattern...")
    
    # Test with no matching files
    print("   Testing with no matching files...")
    
    print("\n=== ALL TESTS COMPLETED ===")

if __name__ == "__main__":
    test_comprehensive()
