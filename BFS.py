'''
    Module containing the BFS (breadth-first-search)
'''

from tree import Tree
from node import Node

class BFS:

    def __init__(self):

        self.tree = Tree()
        self.tree.setRoot(Node)