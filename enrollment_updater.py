#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Enrollment Updater - Simple launcher for the simplified enrollment updater
This script provides a GUI application for updating enrollment data across Excel files.
It matches CRN values between source and target files and updates the Current Enroll column
with values from the Actual column.
"""

import os
import sys
import tkinter as tk
from tkinter import messagebox

# Add the autoenroll directory to the system path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'autoenroll'))

# Import the simple_updater module
try:
    from autoenroll.simple_updater import ExcelDataReplacer
except ImportError:
    messagebox.showerror("Error", "Could not import the simple_updater module.\n"
                        "Make sure the 'autoenroll' directory and 'simple_updater.py' are available.")
    sys.exit(1)

def main():
    """Main function to run the simplified enrollment updater application"""
    try:
        # Create the root window
        root = tk.Tk()
        
        # Set window title and icon
        root.title("Enrollment Updater - Simplified")
        
        # Create the application instance
        app = ExcelDataReplacer(root)
        
        # Run the application
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()