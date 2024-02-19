class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Method to insert node to list
    def insert(self, data=None):
        ni = Node(data)
        if self.head is None:
            ni.next = ni
            self.head = ni
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = ni
            ni.next = self.head

    # Method to iterate through the list a specific number of times, from a specific node and return the resulting node.
    def iterate(self, node, count=None):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            if temp.data == node:
                break
        while 0 < count:
            temp = temp.next
            if temp.data == node:
                continue
            else:
                count -= 1    
        return temp.data