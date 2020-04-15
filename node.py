'''
    Module containing a general Node class
'''

from typing import List, Union

NUM = Union[int, str]

class Node:

    def __init__(self):
        self.parent = None
        self.leftNode = None
        self.rightNode = None
        self.value = None
        self.count = 1

    def getParent(self) -> Node:
        return self.parent

    def getLeftNode(self) -> Node:
        return self.leftNode

    def getRightNode(self) -> Node:
        return self.rightNode

    def getValue(self) -> NUM:
        return self.value

    def setParent(self, newParent: Node):
        self.parent = newParent

    def setLeftNode(self, newNode: Node):
        self.leftNode = newNode

    def setRightNode(self, newNode: Node):
        self.rightNode = newNode

    def setValue(self, value: NUM):
        self.value = value

    def getCount(self);
        return self.count

    def incCount(self):
        self.count += 1

    def decCount(self):
        self.count += 1