# Enrollment Updater v1.0.0

The initial release of the Enrollment Updater tool, featuring a digitally signed Windows executable.

## Features

- Easy-to-use graphical interface for updating enrollment data
- Support for both single file and batch processing modes
- Automatic matching of CRN (Course Registration Number) between files
- Updates "Current Enroll" values with "Actual" enrollment numbers
- Detailed update reports with before/after values
- Digitally signed executable for enhanced security

## What's Included

- `Enrollment_Updater.exe` - Digitally signed Windows executable
- Installation and usage documentation
- Sample input/output files
- License and antivirus information

## Requirements

- Windows operating system
- Microsoft Excel

## Installation

1. Download `Enrollment_Updater_Package.zip`
2. Extract the package to your desired location
3. Run `Enrollment_Updater.exe`

## Documentation

See the included README.md and INSTALL.md files for detailed usage instructions.

## File Format Requirements

### Source File
- Must have a column named 'CRN' or "'CRN'" (with quotes)
- Must have a column named 'Actual' or "'Actual'" (with quotes)

### Target File
- Must have a column named 'CRN'
- Must have a column named 'Current Enroll'

## Security

This release is digitally signed for enhanced security. You can verify the signature through Windows File Properties.
