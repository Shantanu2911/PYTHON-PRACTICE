import turtle

#turtle.Screen().bgcolor("black")

t = turtle.Turtle()
t.speed(5)
t.pensize(20)
t.penup()

def draw_circle():
    t.setposition(0,-250)
    t.pendown()
    t.begin_fill()
    t.color("white")
    t.pencolor("black")
    t.circle(250)
    t.end_fill()
    t.penup()

#

def draw_line():
    t.setposition(250,0)
    t.pendown()
    t.pencolor("black")
    t.left(180)
    # t.forward(300)
    # t.left(120)
    # t.forward(80)
    # t.left(110)
    # t.forward(300)
    # t.right(135)
    t.forward(200)
    t.pos()
    for i in range(100):
        t.left(1)
        t.forward(2)

draw_circle()
draw_line()
turtle.done()
