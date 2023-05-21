__doc__ = """Write a function is_prime that takes 1 argument - a number from 2 to 1000, 
and returns True if it is a prime number, and False otherwise."""
def is_prime(num: int) -> int:
    if num < 2 or num > 1000:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
