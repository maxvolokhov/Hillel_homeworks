___doc___ = """Implement your own print function. It should work on all operating systems. 
You can't use build-in print function"""

import sys

def print_analogue(*args, sep=' ', end='\n', file=sys.stdout):
    output = sep.join(str(arg) for arg in args) + end
    file.write(output)
    file.flush()

if __name__ == '__main__':
    print_analogue('Any input')
