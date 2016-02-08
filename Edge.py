from Vector3D import Vector3D


class Edge:
    def __init__(self, vec, p0=None, p1=None):
        self.vec = vec
        self.p0 = p0
        self.p1 = p1

    def addPoint(self, p):
        if self.p0 is None:
            self.p0 = p
        else:
            assert(self.p1 is None)
            self.p1 = p

