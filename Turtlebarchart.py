def bar_graph(somu,value):
    somu.begin_fill()
    somu.left(90)
    somu.forward(value)
    somu.write(" "+str(value))
    somu.right(90)
    somu.forward(40)
    somu.right(90)
    somu.forward(value)
    somu.left(90)
    somu.end_fill()
    somu.forward(10)

import turtle
t = turtle.Turtle()
a = turtle.Screen()
a.bgcolor("lightblue")
t.color("black" , "orange")
t.pensize(3)
measureheight=[30,40,50,70,80,100]
for i in measureheight:
    bar_graph(t,i)

