'''
8.Use a for loop,range and turtle to draw a spiral.
'''

import turtle
t = turtle.Turtle()

for i in range(100):
    t.pensize(3)
    t.pencolor('grey')
    t.speed(10)
    a = turtle.Screen()
    a.bgcolor("brown")
    t.circle(10+i,50)

    turtle.done
    

