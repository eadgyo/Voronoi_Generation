from Site import Site
from VSite import VSite
from Vector3D import Vector3D
import math
from Edge import Edge


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

def createEdge(p0, p1):
    vec = p1.point - p0.point
    edge = Edge(Vector3D(-vec.getY(), vec.getX()))
    p0.edges.append(edge)
    p1.edges.append(edge)
