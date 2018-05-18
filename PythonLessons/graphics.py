# This is how you would iport the Turtle module
import turtle
'''
# This move the line forward in 90 degrees
turtle.forward (90)
turtle.right(120)
turtle.forward (90)
'''
# Drawing a square
# This repeat the coordinate 4 time from the array
alex = turtle.Turtle()
for i in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)
