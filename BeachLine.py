from Node import Node
from Vector3D import Vector3D
import math

class BeachLine:
    def __init__(self):
        self.root = None

    def insert(self, p0, edges):
        if self.root is None:
            self.root = Node(p0)
            return [None, None, None]
        else:
            return self.root.insert(p0, edges)

    def update(self, ly):
        if self.root is None or self.root.isLeaf():
            return
        self.root.update(ly)

    def remove(self, p0, edges):
        assert(self.root is not None)


        a = self.root.remove(p0, edges)
        if a is None:
            pass
        assert(a is not None)
        return a

    def removeFromVSite(self, vSite, edges):
        return self.remove(vSite, edges)

    def draw(self, screen, x, y, sizeD):
        if self.root is not None:
            self.root.draw(screen, x, y, sizeD)

    def array(self):
        l = []
        if self.root is not None:
            self.root.array(l)
        return l
