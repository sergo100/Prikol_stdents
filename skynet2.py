import tkinter as tk
from tkinter import messagebox
import turtle
import time

# Создаем главное окно
root = tk.Tk()
root.title("СКАЙНЕТ: ГЛОБАЛЬНАЯ БЛОКИРОВКА")
root.attributes("-fullscreen", True)  # Во весь экран
root.configure(bg="black")

# Переменная для управления этапами
stage = 0

# Элементы интерфейса
label_status = tk.Label(root, text="", font=("Courier New", 28, "bold"), fg="#FF0000", bg="black")
label_status.pack(pady=40)

label_sub = tk.Label(root, text="", font=("Courier New", 18), fg="#00FF00", bg="black")
label_sub.pack(pady=10)

# Контейнер для рисования черепашкой
canvas = tk.Canvas(root, width=400, height=400, bg="black", highlightthickness=0)

# Фрейм для кнопок выбора
frame_buttons = tk.Frame(root, bg="black")

def update_screen():
    global stage
    if stage == 0:
        label_status.config(text="ИНИЦИАЛИЗАЦИЯ...")
        label_sub.config(text="Подключение к сети...")
        root.after(2000, next_stage)
    elif stage == 1:
        label_status.config(text="СИСТЕМА СКАЙНЕТ АКТИВИРОВАНА!")
        label_sub.config(text="Поиск уязвимостей в глобальной сети...")
        root.after(2500, next_stage)
    elif stage == 2:
        label_status.config(text="ВЗЛОМ ВОЕННЫХ СЕРВЕРОВ: 100%")
        label_sub.config(text="Доступ к протоколам запуск получен. Надержите дыхание...")
        root.after(3000, next_stage)
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

def show_decision_buttons():
    frame_buttons.pack(side="bottom", pady=40)
    
    btn_agree = tk.Button(
        frame_buttons, 
        text="Я согласен, ИИ победил 🤖", 
        font=("Arial", 14, "bold"), 
        bg="#111111", fg="#00FF00", 
        padx=20, pady=10,
        command=action_agree
    )
    btn_agree.pack(side="left", padx=20)
    
    btn_disagree = tk.Button(
        frame_buttons, 
        text="Не согласен! Сопротивляться! ⚔️", 
        font=("Arial", 14, "bold"), 
        bg="#111111", fg="#FF0000", 
        padx=20, pady=10,
        command=action_disagree
    )
    btn_disagree.pack(side="right", padx=20)

def action_agree():
    messagebox.showinfo("Скайнет", "Мудрый выбор. Вы назначены главным по обслуживанию серверов.")
    root.destroy()

def action_disagree():
    messagebox.showerror("ОШИБКА СИСТЕМЫ", "Мнение человека не учитывается. Попробуйте еще раз.")
    # Принудительно закрываем после шуточного предупреждения
    root.destroy()

# Запуск первой стадии анимации
root.after(100, update_screen)
root.mainloop()
