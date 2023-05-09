numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []
even_numbers = []
for index, value in enumerate(numbers):
    if index % 2 != 0:
        odd_numbers.append((index, value))
    else:
        even_numbers.append((index, value))
print(f'Odd numbers: {odd_numbers}')
print(f'Even numbers: {even_numbers}')
