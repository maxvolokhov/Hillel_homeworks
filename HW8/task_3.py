___doc___ = """Find all of the numbers from 1-1000 that are divisible by 7"""


s = (number for number in range(1, 1000) if number % 7 == 0)
for i in s:
    print(i)
