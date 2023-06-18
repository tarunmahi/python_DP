class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
    def hash_func(self,key):
        return hash(key)%self.size
    def insert(self,key,value):
        index=self.hash_func(key)
        bucket=self.table[index]
        
        for i in range(len(bucket)):
            exis_key,exis_val=bucket[i]
            if key==exis_key:
                bucket[i]=((key,value))
        bucket.append((key,value))
    def get(self,key):
        index=self.hash_func(key)
        bucket=self.table[index]
        
        for i in range(len(bucket)):
            exis_k,exis_v=bucket[i]
            if key==exis_k:
                return exis_v
        return None
    def remove(self,key):
        index=self.hash_func(key)
        bucket=self.table[index]
        
        for i in range(len(bucket)):
            exis_key,exis_val=bucket[i]
            if key==exis_key:
                del bucket[i]

    def display(self):
        for i in range(len(self.table)):
            bucket=self.table[i]
            print(f"the value of bucket{i} is {bucket}")
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
