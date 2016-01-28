from Site import Site
from VSite import VSite
from BeachLine import BeachLine
from Vector3D import Vector3D
import math

class Fortune:
    def __init__(self, points):
        self.points = points
        self.sites = []
        self.events = []
        self.beachLine = BeachLine()

        # Sort Y
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                if self.points[i].getY() < self.points[j].getY():
                    self.points[i], self.points[j] = self.points[j], self.points[i]

        # Convert points into sites and create events
        for i in range(len(self.points)):
            site = Site(self.points[i])
            self.sites.append(site)
            self.events.append(site)

        #self.create()

    def create(self):
        while len(self.events) != 0:
            if type(self.events[len(self.events)-1]) == VSite:
                self.handleVertex()
            else:
                self.handleSite()

    def findMinCircle(self, p1, p2, p3):
        x1 = p1.point.getX(); x1_2 = x1*x1; x2 = p2.point.getX(); x2_2 = x2*x2; x3 = p3.point.getX(); x3_2 = x3*x3;
        y1 = p1.point.getY(); y1_2 = y1*y1; y2 = p2.point.getY(); y2_2 = y2*y2; y3 = p3.point.getY(); y3_2 = y3*y3;

        #First part
        h = x2_2 + y2_2 - (y1_2 + x1_2)
        b = 2*(x2 - x1)
        a = (y1 - y2)

        #Second Part
        f = x3_2 + y3_2 - (y1_2 + x1_2)
        d = 2*(y3 - y1)
        e = (x1 - x3)

        #Determine Center
        x = ((2*a*f/d) + h)/(b*(1-(4*a*e/(d*b))))
        y = (2*x*e + f)/d

        center = Vector3D(x, y)
        magn = math.sqrt((x - x1)*(x - x1) + (y - y1)*(y - y1))
        minY = Vector3D(x, y + magn)

        vSite = VSite(minY, center)
        return vSite

    def insertBeachLine(self, p0):
        pass

    def handleSite(self):
        site = self.events.pop(len(self.events)-1) #SweapLine
        [p1, p, p3] = self.beachLine.insert(site)
        if p1 is not None and p is not None and p3 is not None:
            if p1 is not None:
                min = self.findMinCircle(p1, p, site)
                if min.point.y > site.point.y:
                    self.addEvent(min)
            if p3 is not None:
                min = self.findMinCircle(p1, p, site)
                if min.point.y > site.point.y:
                    self.addEvent(min)

    def handleVertex(self):
        vSite = self.events.pop(len(self.events)-1)

    def addEvent(self, site):
        pass