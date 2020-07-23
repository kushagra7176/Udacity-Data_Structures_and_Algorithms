import hashlib
import datetime
utc = datetime.datetime.utcnow()

def calc_hash(data,timestamp):
      sha = hashlib.sha256()

      hash_str =  data.encode('utf-8') + str(timestamp).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous = None
      self.previous_hash = previous_hash
      self.hash = calc_hash(str(data), self.timestamp)

    def __repr__(self):
        return (
            f"Block []: {repr(self.data)}\n"
            f"Hash: {repr(self.hash)}\n"
            f"Previous Hash: {repr(self.previous_hash)}\n"
            f"{repr(self.timestamp)}\n"
        )

class Blockchain:

    def __init__(self):
        self.head = None

    def size(self):
        size = 0
        temp = self.head
        while temp:
            size = size + 1
            temp = temp.previous
        return size

    def toList(self):
        List = []
        block = self.head
        while block:
            List.append(block)
            block = block.previous
        return List

    def append(self, data, previous_hash):
        if self.head is None:
            self.head = Block(utc, data, 0)
            return
        new_head = Block(utc, data, self.head.hash)
        new_head.previous = self.head
        self.head = new_head

print("Test Case 1 Empty BlockChain")
A = Blockchain()
print("size:", A.size())
print(A.head)
print()

print("Test Case 2 One item BlockChain")
B = Blockchain()
B.append("Genesis", 0)
print("size:", B.size())
for item in B.toList():
    print(item)
print()

print("Test Case 4 Five item BlockChain")
C = Blockchain()
C.append("Genesis", 0)
C.append("Exodus", calc_hash("Genesis", utc))
C.append("Leviticus", calc_hash("Exodus", utc))
C.append("Numbers", calc_hash("Leviticus", utc))
C.append("Deuteronomy", calc_hash("Numbers", utc))

print("size", C.size())
for item in C.toList():
    print(item)