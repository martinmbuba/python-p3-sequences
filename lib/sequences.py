#!/usr/bin/env python3

def print_fibonacci(length):
    """Print a list of the fibonacci sequence up to the given length."""
    if length <= 0:
        print([])
        return
    
    fibonacci_sequence = []
    a, b = 0, 1
    
    for i in range(length):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fib)
    
    print(fibonacci_sequence)
