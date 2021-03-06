README.txt

Program name: File Renamer By Date
Author: Cem Hasan Yesilyurt
Date: 04/04/18
Development Environment: Python 3.6.2

Description:  Some phone apps like Viber generate file names for photos that are a series of long and jumbled characters.  This program takes files that exist in a directory and renames them each with a prefix of the user's choice, followed by a unique file number, followed by the date the file was last modified in the form of YYYY_MM_DD, followed by the file's original extension.  The program follows a model-view-controller architecture and uses methods and functions from the os, os.path, datetime, and tkinter modules.

Files:
- filerenamerscript.py
- filerenamerframe.py
- filerenamercontroller.py (main)

Folders:
- FileRenamerByDate_CY is a directory that contains the executable file "FileRenamerByDate_CY".

Features:
- the program prompts the user for a prefix and path to the folder containing the files to be modified
- the program verifies that the input path exists
- the program verifies that the input prefix does not contain any forbidden characters
- the program checks if any files exist in the input directory
- the program creates copies of the original files, renaming them according to the format stated above
- the program confirms successful completion of the copying/renaming, indicating how many files were processed

Usage:
- download the zip file "FileRenamerByDate_CY" and run the application file (exe) "FileRenamerByDate_CY".  You can place the folder anywhere on your computer and create a shortcut link to the application.
