file_path = 'test/data/created_file.txt'

with open(file_path) as file:
    for line in file:
        elements = line.strip().split(' ')
        left_operand = int(elements[0])
        right_operand = int(elements[1])
        operation = int(elements[2])

        if operation == 1:
            result = left_operand + right_operand
        elif operation == 2:
            result = left_operand - right_operand
        elif operation == 3:
            result = left_operand * right_operand

        print(result)
