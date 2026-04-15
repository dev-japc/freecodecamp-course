"""Simple hash table implementation using string-key hashing.

This module provides a basic HashTable class that stores values in a
dictionary of buckets keyed by the sum of character code points.
It includes add, remove, and lookup operations for string keys.
"""

class HashTable:
    """A very small hash table with bucketed collision handling."""

    def __init__(self):
        """Initialize an empty hash table."""
        self.collection = {}
    
    def __str__(self):
        """Return a readable representation of the hash table."""
        lines = [f'hashed_key: {k} --- value: {v}' for k, v in self.collection.items()]
        return '\n'.join(lines)
    
    def hash(self, string: str):
        """Compute a hash value for a string.

        The hash is the sum of the Unicode code points for each character.

        Args:
            string: The key string to hash.

        Returns:
            An integer hash value.
        """
        hashed_string = 0
        for char in string:
            hashed_string += ord(char)
        return hashed_string

    def add(self, key, value):
        """Add or update a key-value pair in the hash table."""
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value
        

    def remove(self, key):
        """Remove a key and its value from the hash table.

        Args:
            key: The string key to remove.

        Returns:
            None
        """
        key_hash = self.hash(key)
    
        # Check if the hash exists in the collection first
        if key_hash in self.collection:
            # Check if the specific key exists in that bucket
            if key in self.collection[key_hash]:
                del self.collection[key_hash][key]
                
                # Cleanup: If the nested dictionary is now empty, 
                # remove the hash entry entirely to save memory.
            if not self.collection[key_hash]:
                del self.collection[key_hash]
                
        return None

    def lookup(self, key):
        """Retrieve the value associated with a key."""
        hashed_key = self.hash(key)
        if hashed_key in self.collection.keys() and list(self.collection[hashed_key].keys())[0] == key:
            return self.collection[hashed_key][key]
        return None


if __name__ == '__main__':
    table = HashTable()
    table.add('test', 'old value')
    table.add('test', 'new value')
    table.add('test', 'ne555w value')
    table.add('gold', 'metal')
    table.add('golf', 'sport')
    table.remove('golfff')

    print('Hash table contents:')
    print(table)
    print('\nLookup test ->', table.lookup('test'))
