class Node:
    def __init__(self, site):
        self.site = site
        self.left = None
        self.right = None
        self.value = 0
        self.stop = False

    def insert(self, p0):
        magnL = 0
        magnR = 0
        if self.left is not None:
            magnL = self.left.getMagn()
        if self.right is not None:
            magnR = self.right.getMagn()
        if magnL < magnR:
            self.left.insert

    def getY(self):
        return self.site.point.getY()

    def getMagn(self, site):
        v = site.point - self.site.point
        return v.getMagnitude()