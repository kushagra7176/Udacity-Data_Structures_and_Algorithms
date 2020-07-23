class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
class LRU_Cache(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.dictionary = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head

    def get(self,key):
        if key in self.dictionary:
            val = self.dictionary[key]
            self.remove(val)
            self.add(val)
            return val.value
        return -1

    def set(self,key,value):
        if key in self.dictionary:
            self.remove(self.dictionary[key])
        node = Node(key,value)
        self.add(node)
        self.dictionary[key] = node
        if len(self.dictionary) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dictionary[node.key]

    def remove(self,node):
        temp1 = node.next
        temp2 = node.previous
        temp2.next = temp1
        temp1.previous = temp2

    def add(self,node):
        temp1 = self.tail.previous
        temp1.next = node
        self.tail.previous = node
        node.previous = temp1
        node.next = self.tail
#### Test Case 1 ####

print("***Test Case 1***")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))

print("***Test Case 2***")
new_cache = LRU_Cache(2)
new_cache.set(1, 1)
new_cache.set(2, 2)
new_cache.set(1, 10)
print(new_cache.get(1))
print(new_cache.get(2))

print("***Test Case 3***")
new_cache_1 = LRU_Cache(-100)
print("Capacity of cache is ", new_cache_1.capacity)

new_cache_1.set(1, 1)

print(new_cache_1.get(1))
