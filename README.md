# File Splitter Python Script

This README provides a detailed guide for setting up and using the provided Python script to split large text files into smaller parts.

## Overview
The script processes text files in a specified directory, counts their lines, and splits each file into multiple smaller files. It is particularly useful when working with large datasets or log files.

## Features
- Automatically counts the number of lines in each file.
- Splits files into smaller parts based on the desired number of parts.
- Customizable file extensions and input/output directories.
- Displays details about file processing in the console.

## Requirements
- Python 3.7 or higher.
- Input text files stored in the `files/` directory.
- An output directory named `split_files/`.

## Setup Instructions

1. **Prepare Input Files**:
   - Place the text files to be split in a folder named `files` (relative to the script's location).
   - Ensure the files have the specified extension (e.g., `.txt`).

2. **Configure the Script**:
   - Update the `files_count` variable to match the number of files to process.
   - Set `files_extension` to match the extension of the input files (e.g., `.txt`).
   - If necessary, adjust the `number_of_files` variable to control how many parts each file is split into.

3. **Run the Script**:
   - Save the script to a `.py` file.
   - Run the script using Python:
     ```bash
     python main.py
     ```
   - Processed files will be saved in the `split_files/` directory.

## Code Explanation

- **File Line Counting**:
  ```python
  number_of_lines = sum(1 for _ in open('files/' + nstr + files_extension))
  ```
  Counts the total number of lines in the input file.

- **File Reading**:
  ```python
  with open('files/' + nstr + '.mcfunction', 'r') as file:
      lines = file.readlines()
  ```
  Reads all lines from the input file into a list.

- **Lines Per File Calculation**:
  ```python
  lines_per_file = number_of_lines // number_of_files
  remaining_lines = number_of_lines % number_of_files
  ```
  Determines how many lines each output file will contain, accounting for any remainder.

- **File Splitting**:
  ```python
  with open('split_files/' + nstr + '_' + istr + files_extension , 'w') as file:
      number_of_lines_to_write = lines_per_file + (1 if i < remaining_lines else 0)
      for _ in range(number_of_lines_to_write):
          if k < number_of_lines:
              file.write(lines[k])
              k += 1
  ```
  Writes the calculated number of lines to each output file.

## Notes
- Ensure the `files/` directory contains the files to process and `split_files/` exists to store the output.
- The script handles one file at a time, iterating up to `files_count`.
- File extensions for input and output files must match the `files_extension` variable.

## Troubleshooting
- If the script throws an error:
  - Check that the `files/` directory exists and contains files with the specified extension.
  - Verify that the `split_files/` directory exists and is writable.
- If output files are incomplete, ensure `number_of_files` is set to a realistic value based on the size of the input files.

## Example Configuration
Here’s an example setup:

- Input file: `files/0.txt` (contains 100 lines).
- Desired number of output files: 4.
- Script Configuration:
  ```python
  files_count = 1
  files_extension = ".txt"
  number_of_files = 4
  ```
- Output:
  - `split_files/0_0.txt` (25 lines)
  - `split_files/0_1.txt` (25 lines)
  - `split_files/0_2.txt` (25 lines)
  - `split_files/0_3.txt` (25 lines)

Enjoy splitting your files with ease!

