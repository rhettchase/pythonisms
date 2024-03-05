class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value
    
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
    
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a

class Squares:
    def __init__(self, max_root):
        self.max_root = max_root
        self.current = 0

    def __iter__(self):
        # An iterator must return itself as an iterator.
        return self

    def __next__(self):
        # Increment the current number
        self.current += 1
        # Check if we've reached the maximum limit
        if self.current > self.max_root:
            # If so, raise StopIteration
            raise StopIteration
        # Otherwise, return the next square
        return self.current ** 2