"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""


from __future__ import print_function, division

import math
import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # hack: making a slight left turn before starting reduces the error caused by the linear apporximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    arc(t, r, 360)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)
        
if __name__ == '__main__':
    # I hate that the turtle has a human name
    bob = turtle.Turtle()

    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    flower(bob, 10, 40.0, 80.0)
    turtle.mainloop()





    