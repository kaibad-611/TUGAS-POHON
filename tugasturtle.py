import turtle
import random

def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - random.randint(10, 20), t)
        t.left(40)
        draw_tree(branch_length - random.randint(10, 20), t)
        t.right(20)
        t.backward(branch_length)

def draw_flower(t):
    for _ in range(6):
        t.forward(30)
        t.backward(30)
        t.right(60)

def draw_leaf(t):
    t.color("green")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def draw_pot():
    t = turtle.Turtle()
    t.color("brown")
    t.up()
    t.setpos(-20, -150)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(70)
        t.right(90)
    t.end_fill()

def draw_name(name):
    t = turtle.Turtle()
    t.color("black")
    t.up()
    t.setpos(-20, -220)
    t.down()
    t.write(name, font=("Arial", 12, "normal"))

def main():
    t = turtle.Turtle()
    my_screen = turtle.Screen()
    my_screen.bgcolor("pink")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    draw_tree(75, t)

    # Gambar teks nama
    draw_name("KELOMPOK 2")

    # Pindahkan ke posisi bunga
    t.up()
    t.setpos(0, -100)
    t.down()

    my_screen.exitonclick()

if __name__ == "__main__":
    main()
