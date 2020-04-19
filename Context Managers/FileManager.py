class FileManager():
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.open_file = open(self.filename)
        return self.open_file

    def __exit__(self, *exc):
        self.opened_file.close()


with FileManager('README.md') as file:  # FileManager instantiated as object, binds filename to file
    print(file)

from contextlib import contextmanager
@contextmanager  # Creating context manager from function with exactly one yield. Shorter.
def open_file(path, mode):
    the_file = open(path, mode)  # Everything before yield is __enter
    yield the_file  # Everything after yield is __exit__
    the_file.close()
