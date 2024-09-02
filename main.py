import turtle
import random


def draw_heart(t):
    t.color("red", "pink")
    t.begin_fill()
    t.left(50)
    t.forward(100)
    t.circle(40, 180)
    t.left(260)
    t.circle(40, 180)
    t.forward(100)
    t.end_fill()


def draw_rainbow_benzene(t):
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    turtle.bgcolor('black')
    for x in range(360):
        t.pencolor(colors[x % 6])
        t.width(x // 100 + 1)
        t.forward(x)
        t.left(59)


def draw_symmetrical_line(t, x1, y1, x2, y2, axis='x'):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    if axis == 'x':
        t.penup()
        t.goto(x1, -y1)
        t.pendown()
        t.goto(x2, -y2)
    elif axis == 'y':
        t.penup()
        t.goto(-x1, y1)
        t.pendown()
        t.goto(-x2, y2)


def draw_random_shape(t):
    shapes = ['circle', 'square', 'line']
    shape = random.choice(shapes)

    if shape == 'circle':
        radius = random.randint(10, 100)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.penup()
        t.goto(x, y - radius)
        t.pendown()
        t.circle(radius)
    elif shape == 'square':
        side_length = random.randint(20, 100)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(4):
            t.forward(side_length)
            t.right(90)
    elif shape == 'line':
        x1 = random.randint(-200, 200)
        y1 = random.randint(-200, 200)
        x2 = random.randint(-200, 200)
        y2 = random.randint(-200, 200)
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)


def main():
    t = turtle.Turtle()

    while True:
        print("1. Draw Symmetrical Line")
        print("2. Draw Random Shape")
        print("3. Heart")
        print("4. Rainbow Benzene")
        print("5. Exit")
        choice = input("Choose your option: ")

        if choice == '1':
            # Draw a symmetrical line
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            axis = input("Symmetry axis (x/y): ").strip().lower()
            t.reset()
            draw_symmetrical_line(t, x1, y1, x2, y2, axis)
        elif choice == '2':
            t.reset()
            draw_random_shape(t)
        elif choice == '3':
            t.reset()
            draw_heart(t)
        elif choice == '4':
            t.reset()
            draw_rainbow_benzene(t)
        elif choice == '5':
            turtle.bye()
            break
        else:
            print("Invalid choice, please select again.")


if __name__ == "__main__":
    main()
