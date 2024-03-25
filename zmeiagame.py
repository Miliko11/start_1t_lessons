import turtle

def move_forward():
    turtle.forward(50)

def move_backward():
    turtle.backward(50)

def move_left():
    turtle.left(45)

def move_right():
    turtle.right(45)

screen = turtle.Screen()
screen.title("Черепаха реагирует на события")

player = turtle.Turtle()
player.shape('turtle')

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Backward")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")

screen.listen() #подготовка к приему ввода с клавиатуры

turtle.mainloop() #запуск цикла событий
