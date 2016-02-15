from Site import Site
from VSite import VSite
from Vector3D import Vector3D
import math
from Edge import Edge


def findMinCircle(p1, p2, p3):
    x1 = p1.point.getX(); x1_2 = x1*x1; x2 = p2.point.getX(); x2_2 = x2*x2; x3 = p3.point.getX(); x3_2 = x3*x3;
    y1 = p1.point.getY(); y1_2 = y1*y1; y2 = p2.point.getY(); y2_2 = y2*y2; y3 = p3.point.getY(); y3_2 = y3*y3;

    # First part
    h = -(x2_2 + y2_2) + (y1_2 + x1_2)
    b = 2*(x2 - x1)
    a = 2*(y2 - y1)

    # Second Part
    f = -(x3_2 + y3_2) + (y1_2 + x1_2)
    d = 2*(y3 - y1)
    e = 2*(x3 - x1)

    # Determine Center
    t = (d*b - a*e)
    if isNull(t):
        return None

    x = 0
    y = 0
    if isNull(b):
        y = -h/a #a != 0 car pas deux points identiques
        x = -(d*y + f)/e #e != 0 car pas 3 points alignés
    else:
        y = (-f*b + e*h)/t
        x = -(a*y + h)/b

    center = Vector3D(x, y)
    magn = math.sqrt((x - x1)*(x - x1) + (y - y1)*(y - y1))
    minY = Vector3D(x, y + magn)

    vSite = VSite(minY, center)

    vSite.sites.append(p1)
    vSite.sites.append(p2)
    vSite.sites.append(p3)

    return vSite


def computeBreakPoint(p1, p2, ly):
    x1 = p1.point.getX(); x1_2 = x1*x1; x2 = p2.point.getX(); x2_2 = x2*x2
    y1 = p1.point.getY(); y1_2 = y1*y1; y2 = p2.point.getY(); y2_2 = y2*y2
    ly_2 = ly*ly

    # First part
    h = x1_2 + y1_2 - ly_2
    e = 2*(ly - y1)

    # Second Part
    a = 2*(x2 - x1)
    b = 2*(y2 - y1)
    c = x1_2 + y1_2 - x2_2 - y2_2

    if isNull(b):
        if isNull(e):
            return []
        if isNull(a):
            return []
        x = -c/a
        y = (-x*x + 2*x*x1 - h)/e
        return [Vector3D(x, y)]
    else:
        d = -(a*e + 2*b*x1)
        f = -c*e + h*b

        delta = (d*d - 4*b*f)
        if delta < 0.0:
            return []
        elif delta < 0.00001:
            x = -d/(2*b)
            y = (-c -a*x)/b
            return [Vector3D(x, y)]
        else:
            xa = (-d - math.sqrt(delta))/(2*b)
            xb = (-d + math.sqrt(delta))/(2*b)

            # On prend entre les deux
            ya = (-c -a*xa)/b
            yb = (-c -a*xb)/b
            return [Vector3D(xa, ya), Vector3D(xb, yb)]


def createEdge(p0, p1, pointToAdd = None):
    vec = None

    vec = p1.point - p0.point

    vec.normalize()

    edge = Edge(Vector3D(-vec.getY(), vec.getX()))
    p0.edges.append(edge)
    p1.edges.append(edge)

    if pointToAdd is not None:
       edge.addPoint(pointToAdd)

    return edge


def createEdgeIfNot(p0, p1, pointToAdd = None):
    i = 0
    while i != -1 and i < len(p0.edges):
        if p0.edges[i] in p1.edges:
            i = -2
        i += 1

    if i != -1:
        createEdge(p0, p1, pointToAdd)
        return True
    return False


def vertexVerif(min):
    # type 0
    # -------------------------------------
    # ------------------*------------------
    # ------------------p2-----------------
    # -----*-------------------------------
    # -----p1-----------------------*------
    # -----------------------------p3------

    # type 1
    # On regarde sue quelle courbe on est actuellement
    # Pour ca on calcule la collision entre les deux courbes de p1 et p3
    # ------------------------------*------
    # -----*------------------------p3-----
    # -----p1------------------------------
    # -------------------------------------
    # -----------------*-------------------
    # ----------------p2-------------------

    min.sites[0].sites.append(min)
    min.sites[1].sites.append(min)
    min.sites[2].sites.append(min)


def getPosCurve(p, x, y):
    a = p.getY()*p.getY() - y*y
    b = (2*(y - p.getY()))
    if b != 0.0:
        x1 = x + p.getX() - 250
        h = (p.getX() - x1)*(p.getX() - x1) + a
        y1 = -h/b
        return Vector3D(x1, y1)
    else:
        return Vector3D(0, 0)


def isNull(v):
    """
    a = 0.000000001
    return v > -a and v < a
    """
    return v == 0.0

def last():
    """
        def findMinCircle(p1, p2, p3):
            x1 = p1.point.getX(); x1_2 = x1*x1; x2 = p2.point.getX(); x2_2 = x2*x2; x3 = p3.point.getX(); x3_2 = x3*x3;
            y1 = p1.point.getY(); y1_2 = y1*y1; y2 = p2.point.getY(); y2_2 = y2*y2; y3 = p3.point.getY(); y3_2 = y3*y3;

            # First part
            h = x2_2 + y2_2 - (y1_2 + x1_2)
            b = 2*(x2 - x1)
            a = (y1 - y2)

            # Second Part
            f = x3_2 + y3_2 - (y1_2 + x1_2)
            d = 2*(y3 - y1)
            e = (x1 - x3)

            # Determine Center
            x = 0
            if (1-(4*a*e/(d*b))) != 0.0:
                x = ((2*a*f/d) + h)/(b*(1-(4*a*e/(d*b))))


            y = (2*x*e + f)/d

            center = Vector3D(x, y)
            magn = math.sqrt((x - x1)*(x - x1) + (y - y1)*(y - y1))
            minY = Vector3D(x, y + magn)

            vSite = VSite(minY, center)

            vSite.sites.append(p1)
            vSite.sites.append(p2)
            vSite.sites.append(p3)

            return vSite


        def computeBreakPoint(p1, p2, ly):
            x1 = p1.point.getX(); x1_2 = x1*x1; x2 = p2.point.getX(); x2_2 = x2*x2;
            y1 = p1.point.getY(); y1_2 = y1*y1; y2 = p2.point.getY(); y2_2 = y2*y2;
            ly_2 = ly*ly;

            # First part
            h = x1_2 + y1_2 - ly_2
            e = 2*(y1 - ly)

            # Second Part
            a = 2*(x2 - x1)
            b = 2*(y2 - y1)
            c = x1_2 + y1_2 - x2_2 - y2_2

            d = (a - 2*((x1*b)/e))
            f = (((h*b)/e) + c)

            delta = (d*d - 4*b*f/e)
            if delta < 0.0:
                return []
            elif delta < 0.00001:
                x = -d/(2*b/e)
                y = (x*x - 2*x1*x + h)/e
                return [Vector3D(x, y)]
            else:
                xa = (-d + math.sqrt(delta))/(2*b/e)
                xb = (-d - math.sqrt(delta))/(2*b/e)

                # On prend entre les deux
                ya = (xa*xa - 2*x1*xa + h)/e
                yb = (xb*xb - 2*x1*xb + h)/e
                return [Vector3D(xa, ya), Vector3D(xb, yb)]
    """
    pass