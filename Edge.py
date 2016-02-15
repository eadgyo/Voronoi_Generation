from Vector3D import Vector3D


class Edge:
    def __init__(self, vec, p0=None, p1=None):
        self.prec = []
        self.next = []
        self.vec = vec
        self.p0 = p0
        self.p1 = p1
        self.c = False

    def addPoint(self, p):
        if self.p0 is None:
            self.p0 = p
        else:
            assert(self.p1 is None)
            self.p1 = p

    def set(self, p, i):
        if i:
            self.p1 = p
        else:
            self.p0 = p

    def add(self, edge, i):
        if i:
            self.next.append(edge)
        else:
            self.prec.append(edge)

    def test(self):
        if self.p0 is None:
            if len(self.prec) != 0:
                pass
        if self.p1 is None:
            if len(self.next) != 0:
                pass

    def draw(self, screen, fX = 1.0, fY = 1.0, maxX = 10, maxY = 10):
        if self.p0 is not None and self.p1 is not None:
            screen.create_line(self.p0.getX() * fX, self.p0.getY() * fY, self.p1.getX() * fX, self.p1.getY() * fY)


        if self.p0 is not None:
            self.p0.drawF(screen, fX, fY, "Red")


        if self.p1 is not None and self.p0 is not None:
            self.p1.drawF(screen, fX, fY, "Red")


