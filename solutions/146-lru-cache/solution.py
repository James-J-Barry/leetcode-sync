class node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    
    def rem(self):
        self.prev.next = self.next
        self.next.prev = self.prev

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = dict()
        self.capactiy = capacity
        self.head = node()
        self.tail = node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict[key].value
            self.dict[key].rem()
            self.dict.pop(key)
            newNode = node(key, val)
            newNode.next = self.tail
            newNode.prev = self.tail.prev
            self.tail.prev.next = newNode
            self.tail.prev = newNode
            self.dict[key] = newNode
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key].rem()
            self.dict.pop(key)
        if len(self.dict) == self.capactiy:
            k = self.head.next.key
            self.head.next.rem()
            self.dict.pop(k)
        newNode = node(key, value)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.dict[key] = newNode

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)