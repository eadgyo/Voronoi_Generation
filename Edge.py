from Vector3D import Vector3D


class Edge:
    def __init__(self, vec, p0=None, p1=None):
        self.prec = []
        self.next = []
        self.vec = vec
        self.p0 = p0
        self.p1 = p1

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

    def draw(self, screen, fX = 1.0, fY = 1.0, maxX = 10, maxY = 10):
        if self.p0 is not None and self.p1 is not None:
            screen.create_line(self.p0.getX() * fX, self.p0.getY() * fY, self.p1.getX() * fX, self.p1.getY() * fY)
        if self.p0 is not None:
            self.p0.drawF(screen, fX, fY, "Red")
        elif self.p1 is not None:
            p = self.p1
            if self.vec.getY() > self.vec.getX():
                if p.getY() > 0:
                    fac = p.getY()/abs(self.vec.getY())
                    x = p.getX() + fac*self.vec.getX()
                    screen.create_line(p.getX() * fX, p.getY() * fY, x * fX, 0.0)

            else:
                if p.getX() > 0:
                    fac = p.getX()/abs(self.vec.getX())
                    y = p.getY() + fac*self.vec.getY()
                    screen.create_line(p.getX() * fX, p.getY() * fY, 0.0, y * fY)

        if self.p1 is not None:
            self.p1.drawF(screen, fX, fY, "Red")
        elif self.p0 is not None:
            p = self.p0
            if self.vec.getY() > self.vec.getX():
                if p.getY() < maxY:
                    fac = (maxY - p.getY())/abs(self.vec.getY())
                    x = p.getX() + fac*self.vec.getX()
                    screen.create_line(p.getX() * fX, p.getY() * fY, x * fX, maxY * fY)

            else:
                if p.getX() < maxX:
                    fac = (maxX - p.getX())/abs(self.vec.getX())
                    y = p.getY() + fac*self.vec.getY()
                    screen.create_line(p.getX() * fX, p.getY() * fY, maxX * fX, y * fY)