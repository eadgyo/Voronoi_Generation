from Node import Node
from Vector3D import Vector3D
import math

class BeachLine:
    def __init__(self):
        self.root = None

    def insert(self, p0):
        if self.root is None:
            self.root = Node(p0)
            return [None, None, None]
        else:
            return self.root.insert(p0)

    def update(self, ly):
        if self.root is None or self.root.isLeaf():
            return
        self.root.update(ly)

    def remove(self, p0):
        assert(self.root is not None)
        self.root.remove(p0)
