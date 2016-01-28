import numpy
import math

"""
Calcul et Gestion Vector3D
Le vecteur 3D comporte 4 valeurs.
Les 3 premières concernent les coordonnées
La dernière: 0 si c'est un vecteur
             1 si c'est un point
-> Simplification calcul avec les matrices 4x4
"""
class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0, w=1):
        if type(x) == Vector3D:
            self.coor = (y - x).getCoor()
        else:
            self.coor = numpy.array([float(x), float(y), float(z), float(w)])

#====================================================
# Getter
#====================================================
    def copy(self):
        return Vector3D(self.getX(), self.getY(), self.getZ(), self.getW())

    def getTransformation(self, matrix):
        return matrix.dot(self.coor)

    def project(self, projectMatrix):
        return projectMatrix.transform(self)

    def getCoor(self):
        return self.coor

    def getX(self):
        return self.coor[0]

    def getY(self):
        return self.coor[1]

    def getZ(self):
        return self.coor[2]

    def getW(self):
        return self.coor[3]

    def isPoint(self):
        return bool(self.coor[3])

    def getMagnitude(self):
        return math.sqrt(self.getSqMagnitude())

    def getSqMagnitude(self):
        return float(self.scalar(self))
#====================================================
# Setter
#====================================================
    def getNormalize(self):
        vec = self.copy()
        vec.normalize()
        return vec

    def setCoor(self, coor):
        for i in range(4):
            self.coor[i] = coor[i]

    def setX(self, x):
        self.coor[0] = float(x)

    def setY(self, y):
        self.coor[1] = float(y)

    def setZ(self, z):
        self.coor[2] = float(z)

    def setW(self, w):
        self.coor[3] = float(w)

    def set(self, x, y=0, z=0, w=1):
        if type(x) == Vector3D:
            self.setCoor(x.getCoor())
        else:
            self.coor[0] = float(x)
            self.coor[1] = float(y)
            self.coor[2] = float(z)
            self.coor[3] = float(w)

    def setIsPoint(self, isPoint):
        self.coor[3] = (1 if isPoint else 0)

    @staticmethod
    def create(coor): # coor is an array
        return Vector3D(coor[0], coor[1], coor[2], coor[3])

    @staticmethod
    def createFromMatrix(coor):
        return Vector3D(coor[0,0], coor[0,1], coor[0,2], coor[0,3])

#====================================================
# Operators
#====================================================
    def getRotatedZ(self, theta):
        return Vector3D(self.coor[0] * math.cos(theta) - self.coor[1] * math.sin(theta),
                        self.coor[1] * math.cos(theta) + self.coor[0] * math.sin(theta),
                        self.coor[2], self.coor[3])

    def neg(self):
        return Vector3D.create(-self.coor)

    def __neg__(self):
        return self.neg()

    def selfAdd(self, vec3D):
        # marche?
        self.coor += vec3D.getCoor()

    def __iadd__(self, vec3D):
        self.selfAdd(vec3D)
        return self

    def add(self, vec3D):
        nump = self.coor + vec3D.getCoor()
        return Vector3D.create(nump)

    def __add__(self, vec3D):
        return self.add(vec3D)

    def sub(self, vec3D):
        nump = self.coor - vec3D.getCoor()
        return Vector3D.create(nump)

    def __sub__(self, vec3D):
        return self.sub(vec3D)

    def selfSub(self, vec3D):
        self.coor -= vec3D.getCoor()

    def __isub__(self, vec3D):
        self.selfSub(vec3D)
        return self

    def cross(self, vec3D):
        return Vector3D(self.getY()*vec3D.getZ() - self.getZ()*vec3D.getY(),
                       self.getZ()*vec3D.getX() - self.getX()*vec3D.getZ(),
                       self.getX()*vec3D.getY() - self.getY()*vec3D.getX(),
                       self.getZ())

    def __cross__(self, vec3D):
        return self.cross(vec3D)

    def selfCross(self, vec3D):
        self.set(self.getY()*vec3D.getZ() - self.getZ()*vec3D.getY(),
               self.getZ()*vec3D.getX() - self.getX()*vec3D.getZ(),
               self.getX()*vec3D.getY() - self.getY()*vec3D.getX())

    def __icross__(self, vec3D):
        self.selfCross(vec3D)
        return self

    def __mul__(self, f):
        if type(f) == Vector3D:
            return self.scalar(f)
        else:
            return self.multiply(f)

    def __imul__(self, f):
        assert(type(f) != Vector3D)
        self.selfMultiply(f)
        return self

    def __str__(self):
        return str(self.coor)

    def scalar(self, vec3D):
        return self.getX()*vec3D.getX() + self.getY()*vec3D.getY() + self.getZ()*vec3D.getZ()

    def multiply(self, s1):
        s = float(s1)
        return Vector3D(self.coor[0]*s, self.coor[1]*s, self.coor[2]*s, self.coor[3])

    def multiplyVec(self, vec):
        return Vector3D(self.coor[0]*vec.getX(), self.coor[1]*vec.getY(), self.coor[2]*vec.getZ(), self.coor[3])

    def selfMultiply(self, s1):
        s = float(s1)
        for i in range(3):
            self.coor[i] *= s

    def normalize(self):
        magn = self.getMagnitude()
        if magn != 0:
            self.selfMultiply(1.0/magn)
        return magn

    def disp(self):
        print(self)

    @staticmethod
    def createVec(v1, v2):
        return v2.sub(v1)

    def draw(self, screen, color = "black"):
        screen.create_oval(self.getX() - 5, self.getY() - 5, self.getX() + 5, self.getY() + 5, fill=color)
        #screen.create_line(self.getX(), self.getY(), self.getX(), self.getY() + 1)