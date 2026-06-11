import turtle

# Настройка экрана
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Чебурашка на Python Turtle")

t = turtle.Turtle()
t.speed(0)  # Максимальная скорость рисования

def draw_circle(color, radius, x, y):
    """Функция для рисования закрашенного круга"""
    t.penup()
    t.goto(x, y - radius)  # Смещение, чтобы x,y были центром круга
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# 1. ТЕЛО
draw_circle("#8B4513", 70, 0, -120)  # Коричневое тело
draw_circle("#CD853F", 50, 0, -110)  # Светлый животик

# 2. ОГРОМНЫЕ УШИ
# Левое ухо (внешнее коричневое и внутреннее розовое)
draw_circle("#8B4513", 55, -120, 60)
draw_circle("#FFB6C1", 35, -120, 60)

# Правое ухо (внешнее коричневое и внутреннее розовое)
draw_circle("#8B4513", 55, 120, 60)
draw_circle("#FFB6C1", 35, 120, 60)

# 3. ЛАПКИ
# Нижние лапы (ножки)
draw_circle("#8B4513", 25, -40, -150)
draw_circle("#8B4513", 25, 40, -150)

# Ручки
draw_circle("#8B4513", 22, -80, -60)
draw_circle("#8B4513", 22, 80, -60)

# 4. ГОЛОВА
draw_circle("#8B4513", 75, 0, 50)     # Коричневая голова
draw_circle("#FFF8DC", 55, 0, 45)     # Желтовато-кремовая мордочка

# 5. ГЛАЗА
# Левый глаз (белок, зрачок, блик)
draw_circle("white", 12, -22, 65)
draw_circle("black", 7, -22, 65)
draw_circle("white", 2, -20, 68)

# Правый глаз (белок, зрачок, блик)
draw_circle("white", 12, 22, 65)
draw_circle("black", 7, 22, 65)
draw_circle("white", 2, 24, 68)

# 6. НОСИК
draw_circle("black", 4, 0, 45)

# 7. РОТИК (УЛЫБКА)
t.penup()
t.goto(-15, 30)
t.setheading(-60)
t.pendown()
t.pensize(3)
t.pencolor("red")
t.circle(17, 120)  # Дуга для улыбки

# Прячем черепашку и оставляем окно открытым
t.hideturtle()
screen.mainloop()
