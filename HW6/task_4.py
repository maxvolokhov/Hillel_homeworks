__doc__ = """You have a file of unknown length. Write a function that 
will remove all numbers from each line of the file."""
import re
def remove_numbers_from_file(filename: str):
    with open(filename) as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_line = re.sub(r'\d', '', line)
        modified_lines.append(modified_line)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)

filename = r'./test.txt'
# in line above path to file
remove_numbers_from_file(filename)
