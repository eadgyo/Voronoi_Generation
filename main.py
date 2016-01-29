from tkinter import *
from Fortune import Fortune
from Vector3D import Vector3D
import math
"""
def clavier(event):
    global coords

    touche = event.keysym
    canvas.delete(ALL)


    #Analisis
    if len(events) != 0:
        if events[0][1].getY() < lY.getY():
            if events[0][0] == 0: # add site
                a = events.pop(0)
                addSite(a, vec, lY.getY(), )
            elif events[0][0] == 1: # circle event
                pass

    lY.setY(lY.getY() + 5)

    #Check parabola
    checkParabola(vec, beachLine, lY)

    for i in range(len(beachLine)):
        parabola[beachLine[i]][1] = lY.getY()

    for i in range(len(parabola)):
        draw_Pol(canvas, parabola[i][0], parabola[i][1])

    canvas.create_line(0, lY.getY(), lY.getX(), lY.getY())
    for i in range(len(vec)):
        vec[i].draw(canvas)

def addSite(a, vec, ly, beachLine, parabola, actual):
    parabola.append([a[1], ly + 0.1])
    beachLine.append(len(parabola) - 1)
    actual[0] += 1
    if actual[0] < len(vec):
        events.append([0, vec[actual[0]]])

def checkParabola(vec, beachLine, lY):
    x = len(beachLine) - 1
    while x > -1:
        a = vec[beachLine[x]]
        j = 0
        while j < x:
            if x != j:
                b = vec[beachLine[j]]

                veca = b-a
                magn = veca.getMagnitude()

                #print(magn)
                print(lY.getY() - b.getY())
                if lY.getY() - b.getY() > magn:
                    beachLine.pop(j)
                    j -= 1
                    x -= 1
                    break
            j += 1
        x -= 1

def draw_Pol(screen, p, y):
    fac = 10
    a = p.getY()*p.getY() - y*y
    b = (2*(y - p.getY()))
    for x in range(500):
        x1 = x + p.getX() - 250
        h = (p.getX() - x1)*(p.getX() - x1) + a
        y1 = -h/b
        screen.create_oval(x1 - 1, y1 - 1, x1 + 1, y1 + 1, fill='black')

if __name__ == "__main__":
    fenetre = Tk()
    canvas = Canvas(fenetre, width=800, height=800, background='white')

    canvas.focus_set()
    canvas.bind("<Key>", clavier)

    fac = Vector3D(60, 60)
    vec = []
    vec.append(Vector3D(3, 2))
    vec.append(Vector3D(4, 3))
    vec.append(Vector3D(5, 5))
    vec.append(Vector3D(6, 6))
    vec.append(Vector3D(2, 6.2))
    vec.append(Vector3D(3.5, 7))


    for i in range(len(vec)):
        vec[i].setX(vec[i].getX() * fac.getX())
        vec[i].setY(vec[i].getY() * fac.getY())
        vec[i].draw(canvas)

    #Start
    lY = Vector3D(500, vec[0].getY())

    actual = [0]
    edges = []
    vertex = []
    parabola = []
    beachLine = []
    events = []

    events.append([0, vec[0]])

    canvas.pack()
    fenetre.mainloop()
"""
def draw_Pol(screen, p, y):
    fac = 10
    a = p.getY()*p.getY() - y*y
    b = (2*(y - p.getY()))
    for x in range(500):
        x1 = x + p.getX() - 250
        h = (p.getX() - x1)*(p.getX() - x1) + a
        y1 = -h/b
        screen.create_oval(x1 - 1, y1 - 1, x1 + 1, y1 + 1, fill='black')

if __name__ == "__main__":
    fenetre = Tk()
    canvas = Canvas(fenetre, width=800, height=800, background='white')

    vec = []
    vec.append(Vector3D(3, 2))
    vec.append(Vector3D(4, 3))
    vec.append(Vector3D(6, 6))
    vec.append(Vector3D(3.5, 7))
    vec.append(Vector3D(2, 6.2))
    vec.append(Vector3D(5, 5))

    fac = Vector3D(60, 60)

    for i in range(len(vec)):
        vec[i].setX(vec[i].getX() * fac.getX())
        vec[i].setY(vec[i].getY() * fac.getY())

    canvas.focus_set()




    #canvas.bind("<Key>", clavier)
    ly = 100
    f = Fortune(vec)
    p = [f.sites[4], f.sites[5]]
    for i in p:
        i.point.draw(canvas)
        draw_Pol(canvas, i.point, ly)

    a = f.computeBreakPoint(p[0], p[1], ly)
    a.draw(canvas)
    print(a)

    canvas.create_line(0, ly, 500, ly)
    canvas.pack()
    fenetre.mainloop()


