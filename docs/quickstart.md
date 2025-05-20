# Quick Start Guide

This guide will help you get started with the Enrollment Updater tool.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/enrollment-updater.git
   cd enrollment-updater
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

   Or install the package directly:
   ```
   pip install .
   ```

## Running the Program

Run the enrollment updater with:
```
python enrollment_updater.py
```

## File Requirements

### Source File Format
The source file should be an Excel file (.xlsx) that contains:
- A column with header 'CRN' or "'CRN'" (with quotes)
- A column with header 'Actual' or "'Actual'" (with quotes) containing enrollment numbers

Example structure:
| 'CRN' | 'Actual' | 'Subject' | ... |
|-------|----------|-----------|-----|
| 61182 | 70       | SOC       | ... |
| 61183 | 56       | SOC       | ... |
| 61184 | 64       | SOC       | ... |

### Target File Format
The target file should be an Excel file (.xlsx) that contains:
- A column with header 'CRN' 
- A column with header 'Current Enroll' that will be updated

Example structure:
| Room # | CRN   | Current Enroll | B9 Max | ... |
|--------|-------|---------------|--------|-----|
|        | 61182 | 60            | 75     | ... |
|        | 61183 | 56            | 75     | ... |
|        | 61184 | 64            | 75     | ... |

## Usage Instructions

### Single File Mode

1. Start the application
2. Select "Process Single Files" (default)
3. Click "Browse" next to "Source File" and select your source Excel file
4. Click "Browse" next to "Target File" and select your target Excel file
5. Click "Update Enrollment" to process the files
6. After processing, a message will show how many rows were updated
7. Click "View Last Updates" to see details of what was changed

### Batch Mode

1. Start the application
2. Select "Process Folder"
3. Click "Browse" next to "Source Dir" and select a folder containing source files
4. Click "Browse" next to "Target Dir" and select a folder containing target files
5. Optionally modify the "Pattern" field (default: *.xlsx)
6. Click "Update Enrollment" to process all matching files
7. After processing, a message will show how many files and rows were updated
8. Click "View Last Updates" to see details of what was changed

## Debug Mode

If you encounter issues:
1. Check the "Debug Mode" checkbox to see more detailed logging
2. Run the process again to view detailed logs of the matching process
