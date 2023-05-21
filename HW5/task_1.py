import os
import random

directory = r'./test/data'
os.makedirs(directory)

list_1 = []
for _ in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operation = random.randint(1, 3)
    list_1.append((left_operand, right_operand, operation))

file_path = os.path.join(directory, 'created_file.txt')
with open(file_path, 'w') as file:
    for tuple_data in list_1:
        line = ' '.join(str(element) for element in tuple_data)
        file.write(line + '\n')
print("Data saved to:", file_path)
