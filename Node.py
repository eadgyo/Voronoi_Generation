class Node:
    def __init__(self, site):
        self.site = site
        self.left = None
        self.right = None
        self.value = 0
        self.stop = False
        self.root = None

    def insert(self, p0):
        if self.value < p0.point.getX():
            if self.left is None:
                self.left = Node(p0)
                self.left.root = self
            else:
                self.left.insert(p0)
        else:
            if self.right is None:
                self.right = Node(p0)
                self.right.root = self
            else:
                self.right.insert(p0)

    def remove(self, p0):
        if self.site is p0:
            assert(self.root is not None)
            assert(self.left is None and self.right is None)

            if self.root.left is self:
                self.root.left = None
            else:
                self.root.right = None
            return True
        else:
            if self.left is None or (not self.left.remove(p0)):
                assert(self.right is not None and self.right.remov(p0))

    def array(self, a):
        if self.left is not None:
            self.left.array(a)

        a.append(self.site)

        if self.right is not None:
            self.right.array(a)