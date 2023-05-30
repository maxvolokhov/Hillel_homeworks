___doc___ = """Create a decorator that prints to the console the name of the function that was called. 
The function should work as intended. For example, create a pair of functions for the arithmetic operations of 
summation and multiplication. When calling these functions, the result of the operation must be returned and the name 
of the function that was called must be displayed in the console with the result. Small hint (__name__)"""


def print_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Function Name:", func.__name__)
        return result

    return wrapper


@print_function_name
def summation(a: int, b: int):
    return a + b


@print_function_name
def multiplication(a: int, b: int):
    return a * b


result1 = summation(6, 11)
print("Result:", result1)

result2 = multiplication(5, 9)
print("Result:", result2)
