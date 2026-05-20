class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    # Hash Function
    def hashFunction(self, key):
        return key % self.size

    # Add Key
    def add(self, key: int) -> None:
        index = self.hashFunction(key)
        bucket = self.table[index]

        # Avoid duplicates
        for val in bucket:
            if val == key:
                return

        bucket.append(key)

    # Remove Key
    def remove(self, key: int) -> None:
        index = self.hashFunction(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                return

    # Check Key Exists
    def contains(self, key: int) -> bool:
        index = self.hashFunction(key)
        bucket = self.table[index]

        for val in bucket:
            if val == key:
                return True

        return False