'''
    Module containing a general Tree class
'''

from typing import List, Union

from node import Node

NUM = Union[int, str]

class Tree:

    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, newRoot: Node):
        self.root = newRoot

    def addNode(self, newNode: Node):
        '''
            add newNode to the tree through self.root

            ex:
                existing values: [1,3,5,9]
                      new value: 4
                         length: 4
        '''
        
        newNodeValue = newNode.getValue()

        if self.root is not None:

            currentNode = self.root
            
            while(True):

                currentNodeValue = currentNode.getValue()

                if newNodeValue < currentNodeValue:  # new node value is < current value
                    if currentNode.getLeftNode is None: 
                        currentNode.setLeftNode(newNode)
                        return currentNode
                    else:
                        currentNode = node.getLeftNode()

                if currentNodeValue < newNodeValue:  # new node value is > current value
                    if currentNode.getRightNode is None: 
                        currentNode.setRightNode(newNode)
                        return currentNode
                    else:
                        currentNode = currentNode.getRightNode()

                else:  # new node value == current value, therefore increment count
                    currentNode.incCount()
                    return currentNode

    def getNode(self, nodeValue: NUM):

        if nodeValue is None:
            raise valueErrror('Cannot get a value of "None"')

        if self.root is not None:

            currentNode = self.root
            
            while(True):

                currentNodeValue = currentNode.getValue()

                if newNodeValue < currentNodeValue:  # new node value is < current value
                    if currentNode.getLeftNode is not None: 
                        currentNode = node.getLeftNode()
                    else:
                        return None

                if currentNodeValue < newNodeValue:  # new node value is > current value
                    if currentNode.getRightNode is not None: 
                        currentNode = currentNode.getRightNode()
                    else:
                        return None

                else:  # new node value == current value, therefore increment count
                    return currentNode
        
        else:
            raise valueErrror('Tree root is None')