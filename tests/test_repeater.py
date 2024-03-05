import pytest

from iterators.repeater import BoundedRepeater, FibonacciIterator, Squares, bounded_repeater

def test_repeater_class():
    words = BoundedRepeater('Hello', 3)
    
    word_list = []
    
    for word in words:
        word_list.append(word)
        
    assert word_list == ['Hello','Hello','Hello']
    
def test_repeater_function():
    
    word_list = []
    
    for x in bounded_repeater("Hi", 4):
        word_list.append(x)
    
    assert word_list == ['Hi', 'Hi', 'Hi', 'Hi']
    
def test_fibonacci():
    fib = FibonacciIterator(10)
    
    fib_sequence = []
    
    for number in fib:
        fib_sequence.append(number)
    
    assert fib_sequence == [1,1,2,3,5,8,13,21,34,55]
    
    
def test_squares():
    squares = Squares(5)
    
    squares_output = []
    
    for square in squares:
        squares_output.append(square)
        
    assert squares_output == [1,4,9,16,25]