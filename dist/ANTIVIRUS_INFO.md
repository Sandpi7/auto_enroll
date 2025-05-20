# Handling Antivirus Warnings with Enrollment Updater

## About Antivirus Warnings

When you download and try to run the Enrollment Updater executable, your antivirus software may flag it as potentially harmful. This is a **false positive** - the program is completely safe.

## Why This Happens

This is a common issue with all programs created with PyInstaller (the tool used to build this executable). The reason is that PyInstaller packs Python code and libraries into a self-contained executable, which can resemble how some malware operates.

## How to Handle This

### McAfee Antivirus (Recommended Method)

McAfee users commonly experience issues with PyInstaller-built applications. Here's how to add an exception:

1. Open McAfee Security
2. Click on "PC Security" or "Real-Time Scanning"
3. Click on "Settings" (gear icon)
4. Select "Excluded Files" or "Exclusions"
5. Click "Add" to create a new exclusion
6. Browse to the location of your Enrollment_Updater.exe file
7. Select the file and confirm
8. Click "Apply" or "OK" to save changes
9. Restart McAfee if prompted
10. Try running the program again

### Windows Defender
1. Open Windows Security
2. Click on "Virus & threat protection"
3. Under "Virus & threat protection settings", click "Manage settings"
4. Scroll down to "Exclusions" and click "Add or remove exclusions"
5. Click the "+" button and select "File"
6. Browse to the Enrollment_Updater.exe file and select it

### Other Antivirus Software
Most antivirus software has a similar "exclusions" or "exceptions" section in its settings.

### Method 2: Run Anyway (If Allowed)

Some antivirus programs allow you to "run anyway" after reviewing the warning:
1. Right-click the file
2. Select "Run anyway" or a similar option
3. Confirm that you trust the file

### Method 3: Disable Real-time Protection Temporarily (Use with Caution)

As a last resort, you can temporarily disable your antivirus protection:
1. Run the program
2. Re-enable your antivirus immediately after running it

## Verifying the Program is Safe

To confirm the program is safe, you can:
1. Run the program on a system with antivirus disabled or with an exception added
2. Observe that it only performs the enrollment updates as described
3. Check that it only accesses the Excel files you specifically select

## Need Help?

If you continue to experience issues with antivirus warnings, please contact your IT department or the software provider for assistance.
