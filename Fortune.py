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
        self.stop = False
        # Sort Y
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                if self.points[i].getY() < self.points[j].getY():
                    self.points[i], self.points[j] = self.points[j], self.points[i]

        # Convert points into sites and create events
        for i in range(len(self.points)):
            site = Site(self.points[i])
            site.name = "p" + str(i)
            self.sites.append(site)
            self.events.append(site)

        #self.create()

    def create(self):
        if self.stop:
           return
        if len(self.events) != 0:
            if len(self.events) == 4:
                pass
            self.beachLine.update(self.events[len(self.events)-1].point.getY())

            if type(self.events[len(self.events)-1]) == VSite:
                #self.stop = True
                self.handleVertex()
            else:
                self.handleSite()

            self.beachLine.update(self.events[len(self.events)-1].point.getY())

    def handleSite(self):
        site = self.events.pop(len(self.events)-1) #SweapLine
        self.rEvents.append(site)
        [p1, p, p3] = self.beachLine.insert(site) # Here <-----------------------

        print("=== Site Ev ===")
        print("Site = " + str(site))
        print("insert-> " + str(p1) + ", " + str(p) + ", " + str(p3))
        print("===============")

        if p is not None:
            if p1 is not None and p3 is not None:
                # On supprime les evenements liés aux anciens points
                self.removeEvent(p1, p, p3)

            # Création du segment
            createEdge(p, site)

            # AJout des breakpoints
            if p1 is not None:
                min = findMinCircle(p1, p, site)
                min.on = p
                if min.point.getY() > site.point.getY():
                    vertexVerif(min)
                    self.addEvent(min)

            if p3 is not None:
                min = findMinCircle(p3, p, site)
                min.on = p
                if min.point.getY() > site.point.getY():
                    vertexVerif(min)
                    self.addEvent(min)

    def handleVertex(self):
        vSite = self.events.pop(len(self.events)-1)

        print("=== Vertex Ev ===")
        print("Sites = " + str(vSite.sites[0]) + ", " + str(vSite.sites[1]) + ", " + str(vSite.sites[2]))
        self.rEvents.append(vSite)

        [p1, pi, pk, p2, on] = self.beachLine.removeFromVSite(vSite)

        print("remove-> " + str(p1) + ", " + str(pi) + ", " + str(pk) + ", " + str(p2))
        print("=================")

        if pi is not None and pk is not None:
            vSite.edges[0].addPoint(vSite.center)
            vSite.edges[1].addPoint(vSite.center)

            self.vertex.append(vSite.center)

            # AJout des breakpoints
            if p1 is not None and (vSite.type == 0 or p1 is not vSite.on):
                # On supprime les evenements liés aux anciens points
                self.removeEvent(p1, pi, vSite)
                min = findMinCircle(p1, pi, pk)
                if min.point.getY() > vSite.point.getY():
                    min.on = on
                    vertexVerif(min)

                    assert(min.type != 1 or vSite.type != 0), "Que faire?"
                    assert(min.on is not None or min.type != 1)

                    self.addEvent(min)

            if p2 is not None and (vSite.type == 0 or p2 is not vSite.on):
                # On supprime les evenements liés aux anciens points
                self.removeEvent(vSite, pk, p2)
                min = findMinCircle(pi, pk, p2)
                if min.point.getY() > vSite.point.getY():
                    min.on = on
                    vertexVerif(min)

                    assert(min.type != 1 or vSite.type != 0), "Que faire?"
                    assert(min.on is not None or min.type != 1)

                    self.addEvent(min)
        else:
            print("normal?")
        # Ajouter controle au cas ou cas déjà traité

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
        i = 0
        while i < len(p.sites):
            if p.sites[i] in p1.sites:
                if p.sites[i] in p3.sites:
                    self.events.remove(p.sites[i])
                    p1.sites.remove(p.sites[i])
                    p3.sites.remove(p.sites[i])
                    p.sites.remove(p.sites[i])
                    i -= 1
            i += 1

