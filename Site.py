from Vector3D import Vector3D
class Site:

    def __init__(self, point):
        self.point = point
        self.sites = []
        self.edges = []
        self.name = ""

    def __str__(self):
        return self.name
        #return "[ " + str(self.point.getX()) + ", " +  str(self.point.getY()) + " ]"

    def copySites(self):
        sites = []
        for i in range(len(self.sites)):
            sites.append(self.sites[i])
        return sites


