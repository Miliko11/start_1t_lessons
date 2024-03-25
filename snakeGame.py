import turtle
import random
import time

delay = 0.1 #Задержка


wn = turtle.Screen()
wn.title("Игра Змейка")
wn.bgcolor("black")
wn.setup(width=600, height=600) # Размер окна
wn.tracer(0) # автоматическое обновление экрана

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("while")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

def go_up():
if head.direction != "down":
    head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if(head.direction=='up'):
        y = head.ycor()
        head.sety(y+20)
    if (head.direction == 'down'):
        y = head.ycor()
        head.sety(y - 20)
    if (head.direction == 'right'):
        x = head.ycor()
        head.setx(x + 20)
    if (head.direction == 'left'):
        x = head.ycor()
        head.setx(x - 20)

wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_right, "d")
wn.onkey(go_left, "a")

while True:
    wn.update()

    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()




turtle.mainloop()