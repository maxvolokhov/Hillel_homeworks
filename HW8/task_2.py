___doc___ = """Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive. 
The solution should work and not freeze your computer."""


def square_even_elements():
    current = 0
    while current <= 1000000000:
        if current % 2 == 0:
            yield current ** 2
        current += 1


squares = square_even_elements()

for square in squares:
    print(square)
