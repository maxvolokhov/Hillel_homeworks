__doc__ = """"Write a function that takes in a string and returns 
the string with all the vowels removed"""

import re

text = "Hello Everybody"
def remove_vowels(string_1: str) -> str:
    vowels_pattern = r'[aeiouAEIOU]'
    vowels = re.sub(vowels_pattern, '', text)
    return vowels

result = remove_vowels(text)
print(result)
