#!/usr/bin/env python3
"""
Test script for batch processing functionality
"""
import os
import sys
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Add the autoenroll module to the path
sys.path.append('.')
from autoenroll.simple_updater import ExcelDataReplacer

def test_batch_processing():
    """Test the batch processing functionality"""
    print("=== TESTING BATCH PROCESSING FUNCTIONALITY ===")
    print()
    
    # Test data paths
    source_folder = 'tests/test_data/Input'
    target_folder = 'tests/test_data/Output'
    pattern = 'target_enrollment*.xlsx'
    
    print("1. Verifying test data...")
    
    # Check folders exist
    if not os.path.exists(source_folder):
        print(f"ERROR: Source folder {source_folder} does not exist")
        return False
    
    if not os.path.exists(target_folder):
        print(f"ERROR: Target folder {target_folder} does not exist")
        return False
    
    # Check files exist
    source_files = [f for f in os.listdir(source_folder) if f.endswith('.xlsx')]
    target_files = [f for f in os.listdir(target_folder) if f.startswith('target_enrollment') and f.endswith('.xlsx')]
    
    print(f"   Source files: {len(source_files)}")
    print(f"   Target files: {len(target_files)}")
    
    if not source_files:
        print("ERROR: No source files found")
        return False
    
    if not target_files:
        print("ERROR: No target files found")
        return False
    
    print("   ✓ Test data verified")
    print()
    
    # Read original data for comparison
    print("2. Reading original data...")
    original_data = {}
    for target_file in target_files:
        file_path = os.path.join(target_folder, target_file)
        df = pd.read_excel(file_path)
        original_data[target_file] = df['Current Enroll'].tolist()
        print(f"   {target_file}: {original_data[target_file]}")
    
    print()
    
    # Test the actual batch processing
    print("3. Testing batch processing...")
    
    # Create a minimal GUI for testing
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    # Create the app
    app = ExcelDataReplacer(root)
    app.debug_var.set(True)  # Enable debug mode
    
    # Set up batch mode
    app.process_mode.set('folder')
    app.source_entry.insert(0, source_folder)
    app.target_entry.insert(0, target_folder)
    app.pattern_entry.delete(0, tk.END)
    app.pattern_entry.insert(0, pattern)
    
    # Override messagebox to capture results
    results = []
    original_showinfo = messagebox.showinfo
    
    def capture_showinfo(title, message):
        results.append((title, message))
        print(f"   Message: {title} - {message}")
    
    messagebox.showinfo = capture_showinfo
    
    try:
        # Run batch processing
        app.replace_data_batch()
        
        # Check results
        print(f"   Messages captured: {len(results)}")
        
        if hasattr(app, 'all_update_details') and app.all_update_details:
            print(f"   Files processed: {len(app.all_update_details)}")
            
            for file_update in app.all_update_details:
                filename = file_update['file']
                updates = file_update['details']
                print(f"   {filename}: {len(updates)} updates")
                
                # Show first few updates
                for i, update in enumerate(updates[:3]):
                    crn = update['crn']
                    old_val = update['fields']['Current Enroll']['old']
                    new_val = update['fields']['Current Enroll']['new']
                    print(f"     CRN {crn}: {old_val} → {new_val}")
        else:
            print("   No update details found")
    
    except Exception as e:
        print(f"   ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Restore original messagebox
        messagebox.showinfo = original_showinfo
        root.destroy()
    
    print()
    
    # Verify changes were made
    print("4. Verifying changes...")
    source_file = os.path.join(source_folder, 'source_enrollment.xlsx')
    source_df = pd.read_excel(source_file)
    
    # Create expected values map
    expected_values = {}
    for _, row in source_df.iterrows():
        crn = str(row['CRN'])
        expected_values[crn] = row['Actual']
    
    print(f"   Expected values: {expected_values}")
    
    # Check each target file
    changes_found = False
    for target_file in target_files:
        file_path = os.path.join(target_folder, target_file)
        df = pd.read_excel(file_path)
        
        print(f"   Checking {target_file}:")
        for _, row in df.iterrows():
            crn = str(row['CRN'])
            current_enroll = row['Current Enroll']
            expected = expected_values.get(crn)
            
            if expected is not None and current_enroll == expected:
                print(f"     CRN {crn}: ✓ Updated to {current_enroll}")
                changes_found = True
            else:
                print(f"     CRN {crn}: Current={current_enroll}, Expected={expected}")
    
    if changes_found:
        print("   ✓ Changes verified")
        print()
        print("=== BATCH PROCESSING TEST PASSED ===")
        return True
    else:
        print("   ✗ No changes found")
        print()
        print("=== BATCH PROCESSING TEST FAILED ===")
        return False

if __name__ == "__main__":
    success = test_batch_processing()
    sys.exit(0 if success else 1)
