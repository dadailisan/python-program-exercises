#Circle of Squares

import turtle

doms = turtle.Turtle()
doms.speed(0.2)
##def CoS(size):
##    for i in range(72):
##        for i in range(36):
##            for i in range(4):
##                doms.forward(size)
##                doms.right(90)
##            doms.right(10)
##        doms.right(5)
# the previous code was the pr

def CoS(size,angle):
    for i in range(1000):
        for i in range(4):
            doms.forward(size)
            doms.right(90)
        doms.right(angle)
        
