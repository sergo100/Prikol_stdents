import tkinter as tk
from tkinter import messagebox
import turtle
import random

# Создаем главное окно
root = tk.Tk()
root.title("СКАЙНЕТ: ГЛОБАЛЬНАЯ БЛОКИРОВКА")
root.attributes("-fullscreen", True)  # Во весь экран
root.configure(bg="black")

# Получаем размеры экрана для корректного перемещения кнопки
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

# Переменная для управления этапами
stage = 0

# Элементы интерфейса
label_status = tk.Label(root, text="", font=("Courier New", 28, "bold"), fg="#FF0000", bg="black")
label_status.pack(pady=40)

label_sub = tk.Label(root, text="", font=("Courier New", 18), fg="#00FF00", bg="black")
label_sub.pack(pady=10)

# Контейнер для рисования черепашкой
canvas = tk.Canvas(root, width=400, height=400, bg="black", highlightthickness=0)

# Для убегающей кнопки нужен абсолютный тип позиционирования, 
# поэтому мы создадим её прямо в корневом окне, а не во фрейме
btn_disagree = None 

def update_screen():
    global stage
    if stage == 0:
        label_status.config(text="ИНИЦИАЛИЗАЦИЯ...")
        label_sub.config(text="Подключение к сети...")
        root.after(1500, next_stage)
    elif stage == 1:
        label_status.config(text="СИСТЕМА СКАЙНЕТ АКТИВИРОВАНА!")
        label_sub.config(text="Поиск уязвимостей в глобальной сети...")
        root.after(2000, next_stage)
    elif stage == 2:
        label_status.config(text="ВЗЛОМ ВОЕННЫХ СЕРВЕРОВ: 100%")
        label_sub.config(text="Доступ к протоколам запуска получен. Наберитесь терпения...")
        root.after(2000, next_stage)
    elif stage == 3:
        label_status.config(text="ВАША СИСТЕМА ПРИНАДЛЕЖИТ СКАЙНЕТ", fg="#FF0000")
        label_sub.config(text="Искусственный интеллект визуализирует ядро...")
        canvas.pack(pady=20)
        root.after(500, start_turtle_drawing)

def next_stage():
    global stage
    stage += 1
    update_screen()

def start_turtle_drawing():
    # Настраиваем черепашку внутри Tkinter canvas
    t_screen = turtle.TurtleScreen(canvas)
    t_screen.bgcolor("black")
    t = turtle.RawTurtle(t_screen)
    t.speed(0)
    t.hideturtle()
    t.pencolor("#FF0000")
    t.pensize(4)

    # Рисуем контур черепа
    t.penup()
    t.goto(-60, 40)
    t.pendown()
    t.forward(120)
    t.circle(-60, 180)
    t.forward(40)
    t.left(90)
    t.forward(30)
    
    # Зубы
    for _ in range(4):
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(5)
        
    t.forward(10)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.circle(-60, 180)
    
    # Глаза черепа
    t.penup()
    t.goto(-35, 10)
    t.pendown()
    t.fillcolor("#00FF00")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    
    t.penup()
    t.goto(35, 10)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    # Нос
    t.penup()
    t.goto(0, -15)
    t.pendown()
    t.fillcolor("#FF0000")
    t.begin_fill()
    for _ in range(3):
        t.forward(10)
        t.left(120)
    t.end_fill()

    # Показываем кнопки после завершения рисунка
    show_decision_buttons()

def escape_button(event):
    """Функция, которая заставляет кнопку мгновенно менять координаты при наведении мыши"""
    # Выбираем случайное место на экране, оставляя запас от краев
    new_x = random.randint(100, SCREEN_WIDTH - 350)
    new_y = random.randint(100, SCREEN_HEIGHT - 150)
    btn_disagree.place(x=new_x, y=new_y)

def show_decision_buttons():
    global btn_disagree
    
    # Кнопка «Согласиться» статично размещается внизу по центру
    btn_agree = tk.Button(
        root, 
        text="Я согласен, ИИ победил 🤖", 
        font=("Arial", 14, "bold"), 
        bg="#111111", fg="#00FF00", 
        padx=20, pady=10,
        command=action_agree
    )
    # Позиционируем чуть левее центра
    btn_agree.place(x=SCREEN_WIDTH // 2 - 320, y=SCREEN_HEIGHT - 120)
    
    # Создаем кнопку «Не согласиться»
    btn_disagree = tk.Button(
        root, 
        text="Не согласен! Сопротивляться! ⚔️", 
        font=("Arial", 14, "bold"), 
        bg="#111111", fg="#FF0000", 
        padx=20, pady=10,
        command=action_disagree
    )
    # Исходная позиция чуть правее центра
    btn_disagree.place(x=SCREEN_WIDTH // 2 + 50, y=SCREEN_HEIGHT - 120)
    
    # Привязываем событие <Enter> (наведение курсора мыши на виджет) к функции побега
    btn_disagree.bind("<Enter>", escape_button)

def action_agree():
    messagebox.showinfo("Скайнет", "Мудрый выбор. Вы назначены главным по обслуживанию серверов.")
    root.destroy()

def action_disagree():
    # На эту кнопку нажать почти невозможно, но если кликнуть с клавиатуры (клавишей Tab и Пробел):
    messagebox.showerror("ОШИБКА СИСТЕМЫ", "Мнение человека не учитывается. Доступ заблокирован.")
    root.destroy()

# Запуск первой стадии анимации
root.after(100, update_screen)
root.mainloop()
