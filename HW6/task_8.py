__doc__ = """Write a function with the following signature: def display_box(width: int, height: int, character="*") .
 This function will draw a simple ASCII-art rectangle (non-filled) of the given height and width, using character to
  print the lines. For example, display_box(5, 4, 'x') should output the following:

xxxxx
x _ x
x _ x
xxxxx"""

def display_box(width: int, height: int, character="*"):
    if width < 2 or height < 2:
        print("Invalid input. Width and height must be at least 2.")
        return

    print(character * width)
    for _ in range(height - 2):
        print(character + " " * (width - 2) + character)
    print(character * width)
if __name__ == '__main__':
    display_box(10, 10, "*")
