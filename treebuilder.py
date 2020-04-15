'''
    Module containing the a tree builder
'''
from typing import List, Union

from tree import Tree
from node import Node

NUM = Union[int, str]

class TreeBuilder:

    '''
    Builds a tree from a given list of values
    '''

    def __init__(self):

        self.tree = Tree()
        self.values = []

    def setValues(self, newValues: List[NUM]):

        self.values = newValues
        self.tree = Tree()  # need to rebuild tree
        
    def build(self):

        for value in self.values:

            newNode = Node()
            newNode.setValue(value)
            self.tree.addNode(newNode)
