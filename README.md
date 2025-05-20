# Enrollment Updater

A simple tool to update enrollment data between Excel files, specifically designed for updating "Current Enroll" values in target files using "Actual" values from source files, matching by CRN (Course Registration Number).

## Features

- Match enrollment data between source and target Excel files
- Update "Current Enroll" column with values from "Actual" column 
- Process single files or entire folders in batch mode
- View detailed reports of all updates made
- Save update reports to text files
- Simple, clean interface

## Requirements

- Python 3.6+
- Required packages:
  - pandas
  - openpyxl
  - tkinter (typically comes with Python)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Sandpi7/enrollment-updater.git
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
2. Choose your source folder containing Excel files
3. Choose your target folder where updated files will be saved
4. Specify a file pattern (default: *.xlsx)
5. Click "Update Enrollment"
6. View the update results using the "View Last Updates" button

## File Format Requirements

### Source File
- Must have a column named 'CRN' or "'CRN'" (with quotes)
- Must have a column named 'Actual' or "'Actual'" (with quotes)

### Target File
- Must have a column named 'CRN'
- Must have a column named 'Current Enroll'

## License

[MIT License](LICENSE)
