import turtle

#turtle that will draw incomplete squares around and around
right = 50 #first
upward = 40 #second
backward = 60 #third
downward = 50 #forth
while right < 200:
    turtle.forward(right)
    right += 20
    turtle.left(90)
    turtle.forward(upward)
    upward += 20
    turtle.left(90)
    turtle.forward(backward)
    backward += 20
    turtle.left(90)
    turtle.forward(downward)
    turtle.left(90)
    downward += 20

right2 = 30 #first
upward2 = 20 #second
backward2 = 40 #third
downward2 = 30 #forth
turtle.left(45)
while right2 < 150:
    turtle.forward(right)
    right2 += 10
    turtle.left(90)
    turtle.forward(upward)
    upward2 += 10
    turtle.left(90)
    turtle.forward(backward)
    backward2 += 10
    turtle.left(90)
    turtle.forward(downward)
    turtle.left(90)
    downward2 += 10    
    
