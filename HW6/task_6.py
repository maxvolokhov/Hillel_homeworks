__doc__ = """Create a function that accepts N parameters of type int. 
Calculate the sum of these parameters and return it"""

def calculation(*args: int) -> int:
    total = sum(args)
    return total


if __name__ == '__main__':
    print(calculation(15, 12, 21, 87, 98765))
