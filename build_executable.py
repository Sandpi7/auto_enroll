# build_executable.py
"""
Script to build the executable for the Enrollment Updater application
"""

import os
import sys
import PyInstaller.__main__

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define paths
main_script = os.path.join(current_dir, 'enrollment_updater.py')
icon_path = None  # You can add an icon file here if you have one

# Check if the main script exists
if not os.path.exists(main_script):
    print(f"Error: Could not find the main script at {main_script}")
    sys.exit(1)

# Create the arguments for PyInstaller
pyinstaller_args = [
    '--name=Enrollment_Updater',
    '--onefile',  # Create a single exe file
    '--windowed',  # Don't show the console window
    '--clean',  # Clean PyInstaller cache
    '--noupx',  # Don't use UPX compression (reduces false positives)
    '--uac-admin',  # Request admin privileges (can reduce AV flags)
    '--add-data=LICENSE;.',  # Include LICENSE file
    '--add-data=README.md;.',  # Include README file
    f'--add-data={os.path.join(current_dir, "autoenroll")};autoenroll',  # Include the autoenroll module
]

# Add icon if available
if icon_path and os.path.exists(icon_path):
    pyinstaller_args.append(f'--icon={icon_path}')

# Add the main script
pyinstaller_args.append(main_script)

print("Building executable with PyInstaller...")
print(f"Main script: {main_script}")
print("Arguments:", " ".join(pyinstaller_args))

# Run PyInstaller
PyInstaller.__main__.run(pyinstaller_args)

print("\nBuild complete! The executable is in the 'dist' folder.")
