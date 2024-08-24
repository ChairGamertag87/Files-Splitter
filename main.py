files_count = 1
files_extension = ".txt"

for n in range(files_count):  # Repeat the following block 100 times
    nstr = str(n)
    i = 0
    k = 0
    number_of_files = 1

    # Count the number of lines in the file
    number_of_lines = sum(1 for _ in open('files/' + nstr + files_extension))

    print(f"The file {nstr} {files_extension} contains {number_of_lines} lines.")

    # Read all the lines from the file and store them in a list
    with open('files/' + nstr + '.mcfunction', 'r') as file:
        lines = file.readlines()

    # Display the content of the list
    print(lines)

    # Calculate the number of lines per file
    lines_per_file = number_of_lines // number_of_files
    remaining_lines = number_of_lines % number_of_files

    while i < number_of_files:
        istr = str(i)

        # Create and open a new file to write
        with open('split_files/' + nstr + '_' + istr + files_extension , 'w') as file:
            # Determine the number of lines to write in this file
            number_of_lines_to_write = lines_per_file + (1 if i < remaining_lines else 0)

            for _ in range(number_of_lines_to_write):
                if k < number_of_lines:
                    file.write(lines[k])
                    k += 1

        i += 1

    n += 1
