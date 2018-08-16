#draw star with size and number of points

import turtle

t = turtle.Pen()

def draw_star(size, points):
    angle = 360/points
    for i in range(0, points):
        t.forward(size)
        t.left(180-angle)
        t.forward(size)
        t.right(180-angle*2)
        
