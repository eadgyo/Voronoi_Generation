from tkinter import *
from Fortune import Fortune
from Vector3D import Vector3D
from VSite import VSite
import time
import math

def clavier(event):
    global coords

    touche = event.keysym
    canvas.delete(ALL)

    if (ly[0]+ 10)/fac.getY()  >= fortune.events[len(fortune.events) - 1].point.getY():
        ly[0] = fortune.events[len(fortune.events) - 1].point.getY()*fac.getY()
        before = fortune.beachLine.array()
        fortune.create()
        """
        print("--- Array ---")
        print(before)
        print(fortune.beachLine.array())
        print("-------------")
        print("")
        """
    else:
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
    """
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
    """

    edges = fortune.edges
    for i in range(len(edges)):
        edges[i].draw(canvas, fac.getX(), fac.getY())
        if edges[i].p1 is not None:
            print("A")
        if edges[i].p0 is not None:
            print("A")

    """
    for i in range(len(fortune.sites)):
        for j in range(len(fortune.sites[i].edges)):
            if fortune.sites[i].edges[j] not in edgesA:
                edgesA.append(fortune.sites[i].edges[j])
                fortune.sites[i].edges[j].draw(canvas, fac.getX(), fac.getY())
    """


    fortune.beachLine.draw(canvas, 1000, 100, 6)





def draw_Pol(screen, p, y):
    fac = 10
    a = p.getY()*p.getY() - y*y
    b = (2*(y - p.getY()))
    if b != 0.0:
        for x in range(500):
            x1 = x + p.getX() - 250
            h = (p.getX() - x1)*(p.getX() - x1) + a
            y1 = -h/b
            screen.create_oval(x1 - 1, y1 - 1, x1 + 1, y1 + 1, fill='black')


if __name__ == "__main__":
    fenetre = Tk()
    canvas = Canvas(fenetre, width=1600, height=900, background='white')

    vec = []
    vec.append(Vector3D(2, 1))
    vec.append(Vector3D(4, 1.1))
    vec.append(Vector3D(5, 2.7))
    vec.append(Vector3D(3, 3))
    vec.append(Vector3D(4.2, 4))
    vec.append(Vector3D(5.2, 5))
    vec.append(Vector3D(3.1, 5.2))
    vec.append(Vector3D(1, 6))
    vec.append(Vector3D(3, 7.2))
    vec.append(Vector3D(5.4, 7))


    fac = Vector3D(60, 60)
    ly = [0]


    canvas.focus_set()
    fortune = Fortune(vec)
    canvas.bind("<Key>", clavier)

    canvas.pack()

    fenetre.mainloop()



