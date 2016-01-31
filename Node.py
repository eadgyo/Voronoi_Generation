from Geom import *

class Node:
    def __init__(self, site = None):
        self.site = site
        self.left = None
        self.right = None
        self.value = 0
        self.stop = False
        self.root = None

    def copy(self):
        copy = Node(self.site)
        copy.left = self.left
        copy.right = self.right
        copy.value = self.value
        copy.stop = self.stop
        copy.root = self.root

    def insert(self, p0):
        if self.isLeaf():
            p = self.site
            p1 = self.lastSite()
            p3 = self.nextSite()
            self.split(p0)
            return [p1, p, p3]
        elif self.value < p0.point.getX():
            return self.left.insert(p0)
        else:
            return self.right.insert(p0)

    def remove(self, p0):
        if p0.sites[1] is self.site:
            pi = self.lastSite()
            if pi in p0.sites:
                pk = self.nextSite()
                if pk in p0.sites:
                    p1 = pi.lastSite()
                    p2 = pk.nextSite()
                    if self.root.left is self:
                        if self.root.root.left is self.root:
                            self.root.root.left = self.root.right
                        else:
                            self.root.root.right = self.root.right
                        self.root.right = self.root.root
                    else:
                        if self.root.root.left is self.root:
                            self.root.root.left = self.root.left
                        else:
                            self.root.root.right = self.root.left
                        self.root.left = self.root.root
                    return [p1, pi, pk, p2]

        if self.isLeaf():
            assert(False), "No site found"
            return [None, None, None, None]
        else:
            l = self.left.remove(p0)
            if l is not None:
                return self.right.remove(p0)
            else:
                return l

    def update(self, ly):
        iNode1 = self.left.max()
        iNode2 = self.right.low()
        c = None
        breakpoints = computeBreakPoint(iNode1.site, iNode2.site, ly)
        """if len(breakpoints) == 2:
            if iNode1.site.point.getY() < iNode2.site.point.getY():
                c = breakpoints[0]
            else:
                c = breakpoints[1]
        else:
            assert(len(breakpoints) != 0)
            c = breakpoints[0]"""
        assert(len(breakpoints) != 0)
        c = breakpoints[0]
        self.value = c.getX()

        if not self.left.isLeaf():
            self.left.update(ly)
        if not self.right.isLeaf():
            self.right.update(ly)


    def isLeaf(self):
        return self.left is None and self.right is None

    def next(self):
        root = self.findRootRight()
        if root is None:
            return None
        else:
            return root.right.low()

    def last(self):
        root = self.findRootLeft()
        if root is None:
            return None
        else:
            return root.left.max()

    def lastSite(self):
        l = self.last()
        if l is None:
            return l
        else:
            return l.site

    def nextSite(self):
        n = self.next()
        if n is None:
            return n
        else:
            return n.site

    def low(self):
        if self.isLeaf():
            return self
        else:
            return self.left.low()

    def max(self):
        if self.isLeaf():
            return self
        else:
            return self.right.max()

    def findRootRight(self):
        if self.root is None:
            return None
        if self.root.left is self:
            return self.root
        else:
            return self.root.findRootRight()

    def findRootLeft(self):
        if self.root is None:
            return None
        if self.root.right is self:
            return self.root
        else:
            return self.root.findRootLeft()

    def split(self, p):
        self.right = Node()
        self.right.left = Node(p)
        self.right.right = Node(self.site)
        self.left = Node(self.site)

        self.left.root = self
        self.right.root = self
        self.right.left.root = self.right
        self.right.right.root = self.right

        self.site = None

        # Set values
        self.value = p.point.getY()
        self.right.value = p.point.getY()

    def __str__(self):
        if self.isLeaf():
            if self.site is None:
                return "Null"
            if self.site.point is None:
                return "No Point"
            return "[ " + str(self.site.point.getX()) + ", " + str(self.site.point.getY()) + " ]"
        else:
            return str(self.value)




