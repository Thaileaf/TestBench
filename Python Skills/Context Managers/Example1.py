# Method 1 of opening files
with open('Whatever.txt', 'r') as f:  # Open returns a context manager
    print('This is method 1:')
    print(f, '\n')  # Prints file descriptor, not lines in file
    for line in f:
        print(line)

# Method 2 of opening files
from contextlib import contextmanager

@contextmanager
def context_manager(filename, mode='r'):
    f = open(filename, mode)
    yield f # Yield will be the 'as' in the with as statements
    f.close()

print(context_manager('Whatever.txt', 'r'), '\n')

with context_manager('Whatever.txt', 'r') as file:
    print('This is method 2:\n', file)
