class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    union_list = LinkedList()
    set1 = set()
    set2 = set()
    if llist_1.head is None and llist_2.head is None:
        return None
    currentNode1 = llist_1.head
    while currentNode1 is not None:
        set1.add(currentNode1.value)
        currentNode1 = currentNode1.next

    currentNode2 = llist_2.head
    while currentNode2 is not None:
        set2.add(currentNode2.value)
        currentNode2 = currentNode2.next

    union_set = set1.union(set2)
    for items in union_set:
        union_list.append(items)
    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    Intersection_list = LinkedList()
    set1 =set()
    set2  =set()

    if llist_1.head is None and llist_2.head is None:
        return None
    currentNode1 = llist_1.head
    while currentNode1 is not None:
        set1.add(currentNode1.value)
        currentNode1 = currentNode1.next

    currentNode2 = llist_2.head
    while currentNode2 is not None:
        set2.add(currentNode2.value)
        currentNode2 = currentNode2.next

    Intersection_set = set1.intersection(set2)

    if len(Intersection_set) == 0:
        return None
    for items in Intersection_set:
        Intersection_list.append(items)
    return Intersection_list


# Test case 1
print("Test Case 1")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("Union List:",union(linked_list_1,linked_list_2))
print ("Intersection List:",intersection(linked_list_1,linked_list_2))

# Test case 2
print("Test Case 2")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("Union List:",union(linked_list_3,linked_list_4))
print ("Intersection List:",intersection(linked_list_3,linked_list_4))

# Test case 3
print("Test Case 3")

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1,65,23]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ("Union List:",union(linked_list_5,linked_list_6))
print ("Intersection List:",intersection(linked_list_5,linked_list_6))
