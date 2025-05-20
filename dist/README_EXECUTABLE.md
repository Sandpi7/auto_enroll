# Enrollment Updater - Executable Version

This is a standalone executable version of the Enrollment Updater tool that doesn't require Python to be installed.

## How to Use

1. Download the `Enrollment_Updater.exe` file
2. Double-click to run the application
3. You'll see a simple interface with the following options:

### Single File Mode (Default)
- Select "Process Single Files" (default)
- Click "Browse" next to "Source File" to select your source Excel file (containing CRN and Actual columns)
- Click "Browse" next to "Target File" to select your target Excel file (containing CRN and Current Enroll columns)
- Click "Update Enrollment" to process the files
- After processing, a message will show how many rows were updated
- Click "View Last Updates" to see details of what was changed

### Batch Mode
- Select "Process Folder"
- Click "Browse" next to "Source Dir" to select a folder containing source files
- Click "Browse" next to "Target Dir" to select a folder containing target files
- Optionally modify the "Pattern" field (default: *.xlsx)
- Click "Update Enrollment" to process all matching files
- After processing, a message will show how many files and rows were updated
- Click "View Last Updates" to see details of what was changed

## File Requirements

### Source File Format
The source file should be an Excel file (.xlsx) that contains:
- A column with header 'CRN' or "'CRN'" (with quotes)
- A column with header 'Actual' or "'Actual'" (with quotes) containing enrollment numbers

### Target File Format
The target file should be an Excel file (.xlsx) that contains:
- A column with header 'CRN' 
- A column with header 'Current Enroll' that will be updated

## Troubleshooting

If you encounter issues:
- Check the "Debug Mode" checkbox to see more detailed logging
- Make sure your Excel files have the required column headers
- If your antivirus flags the program, see the ANTIVIRUS_INFO.md file for guidance
- The program requires Windows 7 or later

## About

This program was created to simplify the process of updating enrollment data between Excel files. It matches CRN values between the files and updates the Current Enroll values in the target file with the Actual values from the source file.
