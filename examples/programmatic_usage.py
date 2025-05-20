"""
Example of how to use the enrollment updater programmatically
"""

import os
import sys
from tkinter import Tk, messagebox

# Add the parent directory to the system path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # Import from the package
    from autoenroll.simple_updater import ExcelDataReplacer
except ImportError:
    print("Error: Could not import the simple_updater module.")
    print("Make sure the 'autoenroll' directory and 'simple_updater.py' are available.")
    sys.exit(1)

def main():
    """Example of how to run the enrollment updater programmatically"""
    # Create Tk root window (required for messagebox)
    root = Tk()
    root.withdraw()  # Hide the main window
    
    try:
        # Set source and target files
        source_file = "path/to/source_file.xlsx"  # Replace with your source file
        target_file = "path/to/target_file.xlsx"  # Replace with your target file
        
        # Create an instance of ExcelDataReplacer
        updater = ExcelDataReplacer(root)
        
        # Process the files
        updated, update_details = updater.process_files(source_file, target_file)
        
        # Show results
        print(f"Updated {updated} rows")
        
        # Show detailed updates if any
        if updated > 0:
            print("\nUpdate Details:")
            for update in update_details:
                print(f"Row {update['row']}: CRN={update['crn']}")
                for field, values in update['fields'].items():
                    old_val = values.get('old', 'N/A')
                    new_val = values.get('new', 'N/A')
                    print(f"  {field}: {old_val} → {new_val}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        # Destroy the root window
        root.destroy()

if __name__ == "__main__":
    main()
