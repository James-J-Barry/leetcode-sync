class MyHashMap:

    def __init__(self):
        self.store = [[]] * 1001

    def put(self, key: int, value: int) -> None:
        hashind = floor(key/1000)
        bucket = self.store[hashind]

        for i in range(len(bucket)):
            k, v = bucket[i]
            if key == k:
                bucket.pop(i)
                break
        bucket.append((key, value))

    def get(self, key: int) -> int:
        hashind = floor(key/1000)
        bucket = self.store[hashind]
        for i in range(len(bucket)):
            k, v = bucket[i]
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        hashind = floor(key/1000)
        bucket = self.store[hashind]
        for i in range(len(bucket)):
            k, v = bucket[i]
            if key == k:
                bucket.pop(i)
                break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)