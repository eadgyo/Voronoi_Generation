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

        """
        if (self.p0 is None and self.p1 is not None) or (self.p0 is not None and self.p1 is None):
            # On regarde les voisins précédents ou suivant
            if len(self.prec) == 0 and len(self.next) == 0:
                print("aa")

            assert(len(self.prec) == 0 or len(self.next) == 0)
            p = self.p0 if self.p0 is not None else self.p1

            A = -1
            if len(self.prec) != 0:
                for i in range(len(self.prec)):
                    if self.prec[i].p0 is not None and self.prec[i].p1 is not None:
                        p1 = self.prec[i].p0 if self.prec[i].p0 is not p else self.prec[i].p1
                        assert(p1 is not p)
                        vec = p - p1
                        s = vec * self.vec
                        if A == 1 and s > 0:
                            print("??qsf")
                        elif A == 0 and s < 0:
                            print("??qsf")
                        if s < 0:
                            A = 1
                        else:
                            A = 0
            if len(self.next) != 0:
                for i in range(len(self.next)):
                    if self.next[i].p0 is not None and self.next[i].p1 is not None:
                        p1 = self.next[i].p0 if self.next[i].p0 is not p else self.next[i].p1
                        assert(p1 is not p)
                        vec = p - p1
                        s = vec * self.vec
                        if A == 1 and s > 0:
                            print("??qsf")
                        elif A == 0 and s < 0:
                            print("??qsf")
                        if s < 0:
                            A = 1
                        else:
                            A = 0


            if A == 1:
                self.vec *= -1
            if A != -1:
                if abs(self.vec.getY()) > abs(self.vec.getX()):
                    if self.vec.getY() < 0.0:
                        if p.getY() > 0:
                            fac = p.getY()/abs(self.vec.getY())
                            x = p.getX() + fac*self.vec.getX()
                            screen.create_line(p.getX() * fX, p.getY() * fY, x * fX, 0.0)
                    else:
                        if p.getY() < maxY:
                            fac = (maxY - p.getY())/abs(self.vec.getY())
                            x = p.getX() + fac*self.vec.getX()
                            screen.create_line(p.getX() * fX, p.getY() * fY, x * fX, maxY * fY)
                else:
                    if self.vec.getX() < 0.0:
                        if p.getX() > 0:
                            fac = p.getX()/abs(self.vec.getX())
                            y = p.getY() + fac*self.vec.getY()
                            screen.create_line(p.getX() * fX, p.getY() * fY, 0.0, y * fY)
                    else:
                        if p.getX() < maxX:
                            fac = (maxX - p.getX())/abs(self.vec.getX())
                            y = p.getY() + fac*self.vec.getY()
                            screen.create_line(p.getX() * fX, p.getY() * fY, maxX * fX, y * fY)
        """


