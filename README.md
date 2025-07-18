# Enrollment Updater

A simple tool to update enrollment data between Excel files, specifically designed for updating "Current Enroll" values in target files using "Actual" values from source files, matching by CRN (Course Registration Number).

## Features

- Match enrollment data between source and target Excel files
- Update "Current Enroll" column with values from "Actual" column 
- Process single files or entire folders in batch mode
- View detailed reports of all updates made
- Save update reports to text files
- Simple, clean interface
- Digitally signed executable for enhanced security

## Requirements

### Using the Pre-built Executable (Recommended)
- Windows operating system
- Microsoft Excel

### Building from Source
- Python 3.6+
- Required packages:
  - pandas
  - openpyxl
  - tkinter (typically comes with Python)

## Installation

### Option 1: Download the Signed Executable (Recommended)
1. Go to the [Releases](../../releases) page
2. Download the latest `Enrollment_Updater_Package.zip`
3. Extract the zip file
4. Run `Enrollment_Updater.exe`

### Option 2: Build from Source
1. Clone this repository:
   ```
   git clone https://github.com/Sandpi7/auto_enroll.git
   ```

2. Install required packages:
   ```
   pip install pandas openpyxl
   ```

## Usage

Run the application:
```
python enrollment_updater.py
```

### Single File Mode

1. Select "Process Single Files" mode
2. Choose your source Excel file (containing CRN and Actual columns)
3. Choose your target Excel file (containing CRN and Current Enroll columns)
4. Click "Update Enrollment"
5. View the update results using the "View Last Updates" button

### Batch Mode

1. Select "Process Folder" mode
2. Choose your source folder containing the enrollment data Excel file
3. Choose your target folder containing the files to be updated
4. Specify a file pattern for target files (default: *.xlsx)
5. Click "Update Enrollment"
6. View the update results using the "View Last Updates" button

**Note**: In batch mode, one source file with enrollment data is used to update multiple target files matching the pattern.

## File Format Requirements

### Source File
- Must have a column named 'CRN' or "'CRN'" (with quotes)
- Must have a column named 'Actual' or "'Actual'" (with quotes)

### Target File
- Must have a column named 'CRN'
- Must have a column named 'Current Enroll'

## License

[MIT License](LICENSE)
