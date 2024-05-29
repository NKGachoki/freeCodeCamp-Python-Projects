"""Module for the creation of a Circular Linked List"""

class Node:
    """Class for instances of nodes in Circular Linked Lists"""
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    """Class for instances of Circular Linked Lists"""
    def __init__(self):
        self.head = None

    def insert(self, data=None):
        """Method to insert node to list"""
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

    def iterate(self, node, count=None):
        """Method to iterate through the list a specific number of times, from a specific node and return the resulting node"""
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            if temp.data == node:
                break
        while 0 < count:
            temp = temp.next
            if temp.data == node:
                break
            else:
                count -= 1
        return temp.data
    