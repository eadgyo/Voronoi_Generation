from Vector3D import Vector3D
class Site:

    def __init__(self, point):
        self.point = point
        self.sites = []
        self.edges = []

    def __str__(self):
        return "[ " + str(self.point.getX()) + ", " +  str(self.point.getY()) + " ]"
