from Site import Site
from VSite import VSite
from BeachLine import BeachLine
from Geom import *
from Vector3D import Vector3D
import math

class Fortune:
    def __init__(self, points, step = False):
        self.init(points, step)

    def init(self, points, step):
        self.alreadyDone = {}
        self.points = []
        for i in points:
            self.points.append(i.copy())

        self.sites = []
        self.events = []
        self.beachLine = BeachLine()
        self.vertex = []
        self.rEvents = []
        self.edges = []
        # Sort Y
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                if self.points[i].getY() < self.points[j].getY():
                    self.points[i], self.points[j] = self.points[j], self.points[i]
                elif self.points[i].getY() == self.points[j].getY():
                    if self.points[i].getX() < self.points[j].getX():
                        self.points[i], self.points[j] = self.points[j], self.points[i]

        # Convert points into sites and create events
        for i in range(len(self.points)):
            site = Site(self.points[i])
            site.name = "p" + str(i)
            self.sites.append(site)
            self.events.append(site)
        if not step:
            self.create()


    def create(self):
        while len(self.events) != 0:
            self.beachLine.update(self.events[len(self.events)-1].point.getY())
            if type(self.events[len(self.events)-1]) == VSite:
                self.handleVertex()
            else:
                self.handleSite()

    def createStep(self):
        if len(self.events) != 0:
            self.beachLine.update(self.events[len(self.events)-1].point.getY())
            if type(self.events[len(self.events)-1]) == VSite:
                self.handleVertex()
            else:
                self.handleSite()
            if len(self.events) > 0:
                self.beachLine.update(self.events[len(self.events)-1].point.getY())

    def handleSite(self):
        site = self.events.pop(len(self.events)-1)  # SweapLine
        if site.name == "p5":
            pass

        self.rEvents.append(site)
        [p1, p, p3] = self.beachLine.insert(site, self.edges)
        """
        print("=== Site Ev ===")
        print("Site = " + str(site))
        print("insert-> " + str(p1) + ", " + str(p) + ", " + str(p3))
        print("===============")
        """
        if p is not None:
            if p1 is not None and p3 is not None:
                # On supprime les evenements liés aux anciens points
                self.removeEvent(p1, p, p3)

            # Création du segment
            # createEdge(p, site)

            # AJout des breakpoints
            #Cas spécial

            if p1 is p3:
                min = findMinCircle(p1, p, site)
                computeBreakPoint(p1, p, min.point.getY())
            else:
                if p1 is not None:
                    min = findMinCircle(p1, p, site)
                    if self.isValidVertex(min) and min.point.getY() >= site.point.getY():
                        vertexVerif(min)
                        self.addEvent(min)

                if p3 is not None:
                    min = findMinCircle(site, p, p3)
                    if self.isValidVertex(min) and min.point.getY() >= site.point.getY():
                        vertexVerif(min)
                        self.addEvent(min)

    def handleVertex(self):
        vSite = self.events.pop(len(self.events)-1)

        """
        print("=== Vertex Ev ===")
        print("Sites = " + str(vSite.sites[0]) + ", " + str(vSite.sites[1]) + ", " + str(vSite.sites[2]))
        """

        self.rEvents.append(vSite)

        [p1, pi, pk, p2] = self.beachLine.removeFromVSite(vSite, self.edges)

        for i in range(len(vSite.sites)):
            vSite.sites[i].sites.remove(vSite)
        """
        print("remove-> " + str(p1) + ", " + str(pi) + ", " + str(pk) + ", " + str(p2))
        print("=================")
        """

        if pi is not None and pk is not None:
            #self.vertex.append(vSite.center)
            # AJout des breakpoints
            if p1 is not None:
                # On supprime les evenements liés aux anciens points
                self.removeEvent(p1, pi, vSite)
                min = findMinCircle(p1, pi, pk)
                if self.isValidVertex(min) and min.point.getY() >= vSite.point.getY():
                    vertexVerif(min)
                    self.addEvent(min)

            if p2 is not None:
                # On supprime les evenements liés aux anciens points
                self.removeEvent(vSite, pk, p2)
                min = findMinCircle(pi, pk, p2)
                if self.isValidVertex(min) and min.point.getY() >= vSite.point.getY():
                    vertexVerif(min)
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


        self.alreadyDone[Fortune.getChain(site)] = True

        # test
        for x in range(len(self.events)-1):
            if self.events[x].point.getY() < self.events[x+1].point.getY():
                print("error")
        self.events.insert(i+1, site)

    @staticmethod
    def getChain(site):

        sites = list(site.sites)
        for i in range(len(sites)):
            for j in range(i+1, len(sites)):
                if int(sites[i].name[1:]) > int(sites[j].name[1:]):
                    sites[i], sites[j] = sites[j], sites[i]


        ch = ""
        for i in range(len(sites)):
            ch += sites[i].name

        return ch


    def removeEvent(self, p1, p, p3):
        i = 0
        while i < len(p.sites):
            if p.sites[i].sites[1] is p:
                if p.sites[i].sites[0] is p1:
                    if p.sites[i].sites[2] is p3:

                        if p.sites[i] in self.events:
                            self.events.remove(p.sites[i])

                        p1.sites.remove(p.sites[i])

                        if p3 is not p1:
                            p3.sites.remove(p.sites[i])
                        if p is not p1 and p is not p3:
                            p.sites.remove(p.sites[i])
                        i -= 1
            i += 1

    def isValidVertex(self, vSite):
        if vSite is None:
            return False
        if Fortune.getChain(vSite) in self.alreadyDone:
            return False

        radius = (vSite.center - vSite.point).getMagnitude()
        i = len(self.sites) - 1
        while i > -1 and vSite.point.getY() >= self.sites[i].point.getY():
            if self.sites[i] not in vSite.sites:
                vec = vSite.center - self.sites[i].point
                if vec.getMagnitude() < radius:

                    return False
            i -= 1
        return True
