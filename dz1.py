import turtle

t = turtle.Turtle()
screen = turtle.Screen()

dict = {"квадрат" :"red", "треугольник" :"blue", "круг" : "green"}

list_colors = dict.values()
for k, v in dict.items():
    t.begin_fill()
    if k == "квадрат":
        for v in range(4):
            t.fillcolor(list(list_colors)[0])
            t.right(90)
            t.forward(50)
        t.end_fill()
    t.penup()
    t.begin_fill()
    if k == "треугольник":
        t.goto(150, 0)
        t.pendown()
        for v in range(3):
            t.fillcolor(list(list_colors)[1])
            t.right(120)
            t.forward(70)
        t.end_fill()
    t.penup()
    t.begin_fill()
    if k == "круг":
        t.goto(50, -150)
        t.pendown()
        t.fillcolor(list(list_colors)[2])
        t.circle(50)
        t.end_fill()

turtle.done()
