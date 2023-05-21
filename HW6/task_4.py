__doc__ = """You have a file of unknown length. Write a function that 
will remove all numbers from each line of the file."""
import re
def remove_numbers_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_line = re.sub(r'\d', '', line)
        modified_lines.append(modified_line)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)

filename = r'./file_to_path'
remove_numbers_from_file(filename)
