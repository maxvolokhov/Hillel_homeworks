___doc___ = """Find all of the numbers from 1-1000 that have a 3 in them"""

findable_number = (number for number in range(1, 1000) if len(str(number)) == 3)
for i in findable_number:
    print(i)
