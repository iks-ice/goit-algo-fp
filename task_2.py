import turtle

def draw_pythagoras_tree(branch_len, level, t):

    if level == 0:
        return

    t.forward(branch_len)

    t.left(45)
    draw_pythagoras_tree(branch_len * 0.707, level - 1, t)

    t.right(90) 
    draw_pythagoras_tree(branch_len * 0.707, level - 1, t)

    t.left(45)
    t.backward(branch_len)

def main():
    try:
        level = int(input("Введіть рівень рекурсії (рекомендовано від 1 до 10): "))
        if level < 0:
            print("Рівень рекурсії не може бути від'ємним.")
            return
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.title("Фрактал: Дерево Піфагора")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)      
    t.left(90)          
    t.color("darkgreen")
    t.pensize(2)

    t.penup()
    t.goto(0, -250)
    t.pendown()

    initial_branch_length = 150

    print("Малюю фрактал...")

    draw_pythagoras_tree(initial_branch_length, level, t)

    t.hideturtle()
    
    screen.exitonclick()

if __name__ == "__main__":
    main()
