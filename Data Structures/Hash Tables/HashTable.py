# Hash tables have a O(1) look up time
# Disadvantages are possible high memory requirement, as excess space is usually needed
# Uses key value pairs
# Similar to dictionaries in Python

class HashTable:

    # Initializes an array with four spaces
    def __init__(self, length=4):
        self.array = [None] * length

    # Hashes a key relative to the length of the array
    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    # Add method adds a key value pair to the array
    def add(self, key, value):
        # Gets the index through the hashing function
        index = self.hash(key)

        # If our array at the index has something already stored there, then we will check if
        # the key is being stored. If not, add it
        # This method of collision handling is called "chaining".
        if self.array[index] is not None:
            for pairs in self.array[index]:
                if pairs[0] == key:
                    pairs[1] = value
                    break
            else:
                # Does not exist, adds it
                self.array[index].append[key, value]

        else:
            # The index is empty, so we will add a new list and append the key and value to there
            self.array[index] = []
            self.array[index].append[key, value]

        #check
        if self.is_full():
            self.double()

    # Gets the value of the key given from the array by looping
    # through index, raising a key error if the index is empty or the key cannot be found
    def get(self, key):
        index = self.hash(key)

        if self.array[index] is not None:
            for pairs in self.array[index]:
                if pairs[0] == key:
                    return pairs[1]
            else:
                raise KeyError()
        else:
            raise KeyError()

    def is_full(self):
        objects = 0
        for obj in self.array:
            if obj is not None:
                objects += len(obj)
        load_factor = len(objects) / len(self.array)
        # If there are more objects than half the length of the total array
        if load_factor > .5:
            return True

    def double(self):
        ht2 = HashTable(length=len(self.array) * 2)
        for index in self.array:
            if index is not None:
                for pair in index:
                    # Adds each key value pair to a hash table of different length
                    # Different hash codes because different length
                    ht2.add([pair[0], pair[1]])
        self.array = ht2.array
