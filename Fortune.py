from Site import Site
from VSite import VSite
from BeachLine import BeachLine
from Geom import *
from Vector3D import Vector3D
import math

class Fortune:
    def __init__(self, points):
        self.points = points
        self.sites = []
        self.events = []
        self.beachLine = BeachLine()
        self.vertex = []
        self.rEvents = []

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
        if len(self.events) != 0:
            if len(self.events) == 4:
                pass
            self.beachLine.update(self.events[len(self.events)-1].point.getY())

            if type(self.events[len(self.events)-1]) == VSite:
                self.handleVertex()
            else:
                self.handleSite()

    def handleSite(self):
        site = self.events.pop(len(self.events)-1) #SweapLine
        self.rEvents.append(site)
        [p1, p, p3] = self.beachLine.insert(site) # Here <-----------------------
        if p is not None:
            if p1 is not None and p3 is not None:
                self.removeEvent(p1, p, p3)
            createEdge(p, site)
            if p1 is not None:
                min = findMinCircle(p1, p, site)
                if min.point.getY() > site.point.getY():
                    self.addEvent(min)

            if p3 is not None:
                min = findMinCircle(p3, p, site)
                if min.point.getY() > site.point.getY():
                    self.addEvent(min)


    def handleVertex(self):
        vSite = self.events.pop(len(self.events)-1)
        self.rEvents.append(vSite)
        [p1, pi, pk, p2] = self.beachLine.removeFromVSite(vSite)

        if pi is not None and pk is not None:
            edge1 = None
            edge2 = None

            i = 0
            while edge1 is None:
                if vSite.edges[i] in pi.edges:
                    edge1 = vSite.edges[i]
                i += 1

            i = 0
            while edge2 is None:
                if vSite.edges[i] in pk.edges:
                    edge2 = vSite.edges[i]
                i += 1

            edge1.addPoint(vSite.center)
            edge2.addPoint(vSite.center)
            self.vertex.append(vSite.center)

            if p1 is not None:
                self.removeEvent(p1, pi, vSite)
                min = findMinCircle(p1, pi, pk)
                if min.point.getY() > vSite.point.getY():
                    self.addEvent(min)

            if p2 is not None:
                self.removeEvent(vSite, pk, p2)
                min = findMinCircle(pi, pk, p2)
                if min.point.getY() > vSite.point.getY():
                    self.addEvent(min)
        else:
            print("normal?")


        #removeEvent

    def addEvent(self, site):
        i = len(self.events) - 1
        while i > -1:
            if site.point.getY() < self.events[i].point.getY():
                break
            i -= 1

        # test
        for x in range(len(self.events)-1):
            if self.events[x].point.getY() < self.events[x+1].point.getY():
                print("error")
        self.events.insert(i+1, site)

    def removeEvent(self, p1, p, p3):
        for i in range(len(p.sites)):
            if p.sites[i] in p1.sites:
                if p.sites[i] in p3.sites:
                    self.events.remove(p.sites[i])
                    p1.remove(p.sites[i])
                    p3.remove(p.sites[i])
                    p.pop(i)

