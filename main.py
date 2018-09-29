from tkinter import *
from Fortune import Fortune
from Vector3D import Vector3D
from VSite import VSite
import time
import math

def step(event):
    global coords

    touche = event.keysym
    canvas.delete(ALL)
    if len(fortune.events) > 0 and (ly[0]+ 10)/fac.getY()  >= fortune.events[len(fortune.events) - 1].point.getY():
        ly[0] = fortune.events[len(fortune.events) - 1].point.getY()*fac.getY()
        before = fortune.beachLine.array()
        fortune.createStep()

        """
        print("--- Array ---")
        print(before)
        print(fortune.beachLine.array())
        print("-------------")
        print("")
        """
    elif len(fortune.events) > 0:
        fortune.beachLine.update(float((ly[0]+ 10))/fac.getY())
        ly[0] += 10
    else:
        fortune.beachLine.update(float((ly[0]+ 10))/fac.getY())
        ly[0] += 10


    canvas.create_line(0, ly[0], 500, ly[0], fill="red")
    for i in range(len(vec)):
        a = vec[i].copy()
        a.setX(vec[i].getX() * fac.getX())
        a.setY(vec[i].getY() * fac.getY())
        a.draw(canvas)


    rE = fortune.rEvents
    for i in range(len(rE)):
        if type(rE[i]) is not VSite:
            a = rE[i].point.copy()
            a.setX(rE[i].point.getX() * fac.getX())
            a.setY(rE[i].point.getY() * fac.getY())
            a.draw(canvas)
            draw_Pol(canvas, a, ly[0])
            canvas.create_text(a.getX() - 10, a.getY()  + 12, anchor=W, font="Arial 8", text=str(rE[i]))

    E = fortune.events
    for i in range(len(E)):
        if type(E[i]) == VSite:
            a = E[i].point.copy()
            a.setX(E[i].point.getX() * fac.getX())
            a.setY(E[i].point.getY() * fac.getY())
            a.draw(canvas, "blue")
            canvas.create_text(a.getX() - 10, a.getY()  - 12, anchor=W, font="Arial 8", text=str(E[i]))
            center = E[i].center.copy()
            center.setX(center.getX() * fac.getX())
            center.setY(center.getY() * fac.getY())
            dist = a.getY() - center.getY()


            canvas.create_oval(center.getX() - dist, center.getY() - dist, center.getX() + dist, center.getY() + dist)
        else:
            a = E[i].point.copy()
            a.setX(E[i].point.getX() * fac.getX())
            a.setY(E[i].point.getY() * fac.getY())
            a.draw(canvas)
            canvas.create_text(a.getX() - 10, a.getY()  + 12, anchor=W, font="Arial 8", text=str(E[i]))


    edges = fortune.edges
    for i in range(len(edges)):
        edges[i].draw(canvas, fac.getX(), fac.getY(), 20, 20)

    """
    for i in range(len(fortune.sites)):
        for j in range(len(fortune.sites[i].edges)):
            if fortune.sites[i].edges[j] not in edgesA:
                edgesA.append(fortune.sites[i].edges[j])
                fortune.sites[i].edges[j].draw(canvas, fac.getX(), fac.getY())
    """


    fortune.beachLine.draw(canvas, 1000, 100, 6)

def full(event):
    if event is not None:
        global coords

        touche = event.keysym
    canvas.delete(ALL)

    canvas.create_line(0, ly[0], 500, ly[0], fill="red")
    for i in range(len(vec)):
        a = vec[i].copy()
        a.setX(vec[i].getX() * fac.getX())
        a.setY(vec[i].getY() * fac.getY())
        a.draw(canvas)


    edges = fortune.edges
    for i in range(len(edges)):
        edges[i].draw(canvas, fac.getX(), fac.getY(), 20, 20)


def clavier(event):
    if start[0]:
        fortune.init(vec, True)
        start[0] = False
        ly[0] = 0
    step(event)

def mouse(event):
    a = Vector3D(float(event.x)/fac.getX(), float(event.y)/fac.getY())

    """
    point = len(vec) - 1
    max = 5
    magn = max + 1.0
    while point > -1 and (vec[point] - a).getMagnitude() > max:
        point -= 1

    if point == -1:
        vec.append(a)
        print("Add")
    ""
    else:
        print("Mo")
        vecA = a - mousePos
        vec[point] += vecA
    ""
    fortune.init(vec, False)
    """
    print(a)
    vec.append(a)
    fortune.init(vec, False)
    fortune.beachLine.update(float(fortune.rEvents[len(fortune.rEvents) - 1].point.getY() + 100)/fac.getY())


    full(event)
    start[0] = True






def draw_Pol(screen, p, y):
    fac = 5
    start = 100
    a = p.getY()*p.getY() - y*y
    b = (2*(y - p.getY()))

    x2 = p.getX() - start*fac
    h = (p.getX() - x2)*(p.getX() - x2) + a
    if b != 0.0:
        y2 = -h/b

        if b != 0.0:
            for x in range(start*2):
                x1 = x*fac + p.getX() - start*fac
                h = (p.getX() - x1)*(p.getX() - x1) + a
                y1 = -h/b
                screen.create_line(x1, y1, x2, y2, fill='black')

                x2 = x1
                y2 = y1


if __name__ == "__main__":
    fenetre = Tk()
    canvas = Canvas(fenetre, width=1600, height=900, background='white')


    vec = []
    #vec.append(Vector3D(6.58333333, 1.1))
    #vec.append(Vector3D(6.1,  2))

    #vec.append(Vector3D(2.96666667, 1.01666667))
    #vec.append(Vector3D(4, 1))
    #vec.append(Vector3D(10.2, 1.58333333))
    #vec.append(Vector3D(11.78333333, 1.25))

    ##[ 10.08333333   4.06666667   0.           1.        ]
    ##[ 11.78333333   1.25         0.           1.        ]

    ##vec.append(Vector3D(9.5, 2.06666667))

    #vec.append(Vector3D(11.41666667,3.61666667))

    #vec.append(Vector3D(6.6, 6.78333333))
    #vec.append(Vector3D(2.88333333, 6.08333333))
    """
    vec.append(Vector3D(5, 2.7))
    vec.append(Vector3D(3.2, 3))
    vec.append(Vector3D(4.2, 4))
    vec.append(Vector3D(5.2, 5.1))
    vec.append(Vector3D(3.1, 5.2))
    vec.append(Vector3D(1, 5))
    vec.append(Vector3D(3, 8.2))
    vec.append(Vector3D(1, 7))
    """

    start = [True]
    for i in vec:
        i.setY(i.getY() +40)
        i.setX(i.getX() + 0)

    fac = Vector3D(15, 15)
    ly = [0]

    mousePos = Vector3D(-1, -1)

    canvas.focus_set()
    fortune = Fortune(vec, True)
    #full(None)

    canvas.bind("<Key>", clavier)
    canvas.bind("<Button-1>", mouse)



    canvas.pack()



    fenetre.mainloop()



