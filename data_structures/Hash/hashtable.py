class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            existing_key, existing_value = bucket[i]
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value

        return None

    def remove(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            existing_key, value = bucket[i]
            if existing_key == key:
                del bucket[i]
                return

    def display(self):
        for i in range(len(self.table)):
            bucket = self.table[i]
            print(f'Bucket {i}: {bucket}')


# Example usage:
hash_table = HashTable(10)

hash_table.insert('apple', 5)
hash_table.insert('banana', 7)
hash_table.insert('orange', 2)

print(hash_table.get('apple'))    # Output: 5
print(hash_table.get('banana'))   # Output: 7
print(hash_table.get('orange'))   # Output: 2
print(hash_table.get('grape'))    # Output: None

hash_table.remove('banana')

hash_table.display()
