___doc___ = """Create an iterator that accepts a sequence and can iterate over values
 over a given range. CustomIterator(sequence, start_index, end_index)"""

class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.end_index = end_index
        self.current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index <= self.end_index:
            value = self.sequence[self.current_index]
            self.current_index += 1
            return value
        else:
            raise StopIteration()


if __name__ == '__main__':
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    start_index = 2
    end_index = 6

    iterator = CustomIterator(sequence, start_index, end_index)

    for value in iterator:
        print(value)
