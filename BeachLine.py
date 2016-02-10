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

    def remove(self, p0):
        assert(self.root is not None)
        a = self.root.remove(p0)
        assert(a is not None)
        return a

    def removeFromVSite(self, vSite):
        p = vSite.sites
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                if p[i].point.getX() > p[j].point.getX():
                    assert(False)
        if vSite.type == 1:
            i = 0
            while vSite.sites[i] is not vSite.on:
                i+=1
            assert(i != 1)
            vSite.sites[i] = vSite.sites[1]
            vSite.sites[1] = vSite.on

        return self.remove(vSite)

    def draw(self, screen, x, y, sizeD):
        if self.root is not None:
            self.root.draw(screen, x, y, sizeD)

    def array(self):
        l = []
        if self.root is not None:
            self.root.array(l)
        return l
