'''
# Draw a polygon

import turtle
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle  =360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()



import turtle
ninja = turtle.Turtle()

ninja.speed(100)
for i in range(180):
    ninja.forward(100)
    ninja.right(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    ninja.penup()
    ninja.setposition(0,0)
    ninja.pendown()
    ninja.right(2)

turtle.done()
'''


#Stackingup Triangles

from turtle import *

size = 800
min=64
pf = 0.8660254 #Pythagoras factor: sqrt(3)/2

def S(l,x,y):
    if l>min: #Not done yet?
        l=l/2 #scale down by 2
        S(l,x,y) #bottom left triangle
        S(l,x+l, y)#bottom right triangle
        S(l,x+l/2, y+l*pf)# top triangle
    else:
        goto(x,y);
        pendown()#start at (x,y)
        begin_fill()
        forward(l);
        left(120)#triangle base
        forward(l);
        left(120) #triangleright
        forward(l);
        end_fill()
        setheading(0) #face East
        penup();
        goto(x, y)

penup()
speed('fastest')
S(size,-size/2, -size*pf/2.0)
done()
