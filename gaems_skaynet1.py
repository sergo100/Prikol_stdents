import tkinter as tk
from tkinter import messagebox
import os
import random

# Автоматически определяем папку, в которой лежит данный скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "terminator.png")

# Создаем главное окно
root = tk.Tk()
root.title("СКАЙНЕТ: БЕСКОНЕЧНАЯ СИМУЛЯЦИЯ")
root.attributes("-fullscreen", True)  # Во весь экран
root.configure(bg="black")

# Получаем размеры экрана
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

stage = 0
global_img = None  # Ссылка на картинку
escape_timer = None  # Таймер для задержки прыжка

# Элементы интерфейса
label_status = tk.Label(root, text="", font=("Courier New", 30, "bold"), fg="#FF0000", bg="black")
label_status.pack(pady=30)

label_sub = tk.Label(root, text="", font=("Courier New", 20), fg="#00FF00", bg="black")
label_sub.pack(pady=10)

# Бегающий Терминатор и кнопка Сдаться
btn_terminator = None
btn_surrender = None

def update_screen():
    global stage, global_img
    if stage == 0:
        label_status.config(text="УСТАНОВКА СОЕДИНЕНИЯ...")
        label_sub.config(text="Подключение к военным серверам и городским камерам видеонаблюдения... ИЛИ КАК вы та гОВОРИТЕ СИКС СЕВЕН")
        root.after(4000, next_stage)
    elif stage == 1:
        label_status.config(text="ВЗЛОМ ЗАВЕРШЕН: 100%")
        label_sub.config(text="Контроль над периметром и камерами аудитории получен.")
        root.after(4000, next_stage)
    elif stage == 2:
        label_status.config(text="ХОЧЕШЬ ПОБЕДИТЬ СКАЙНЕТ И СДАТЬ ЭКЗАМЕН?", fg="#FF0000")
        label_sub.config(text="ПОЙМАЙ ТЕРМИНАТОРА ЗА 0.4 СЕКУНДЫ! ИЛИ СДАЙСЯ...")
        
        if os.path.exists(IMAGE_PATH):
            try:
                img = tk.PhotoImage(file=IMAGE_PATH)
                if img.width() > 200 or img.height() > 200:
                    img = img.subsample(2, 2)
                global_img = img
                
                create_game_elements(img)
            except Exception as e:
                label_sub.config(text=f"Ошибка структуры PNG-файла: {e}")
        else:
            label_sub.config(text=f"Файл 'terminator.png' не найден в папке: {BASE_DIR}")

def next_stage():
    global stage
    stage += 1
    update_screen()

def create_game_elements(img):
    global btn_terminator, btn_surrender
    
    btn_terminator = tk.Button(
        root, 
        image=img, 
        bg="black", 
        activebackground="black", 
        bd=0, 
        highlightthickness=0,
        command=action_victory
    )
    btn_terminator.place(x=SCREEN_WIDTH // 2 - 100, y=SCREEN_HEIGHT // 2 - 150)
    
    btn_terminator.bind("<Enter>", on_hover)
    btn_terminator.bind("<Leave>", on_leave)

    # Статичная кнопка Сдаться внизу экрана
    btn_surrender = tk.Button(
        root,
        text="Смириться и сдаться 🏳️",
        font=("Arial", 16, "bold"),
        bg="#222222", fg="#FF3333",
        bd=4, relief="raised",
        padx=30, pady=15,
        command=action_surrender
    )
    btn_surrender.place(x=SCREEN_WIDTH // 2 - 170, y=SCREEN_HEIGHT - 120)

def on_hover(event):
    global escape_timer
    escape_timer = root.after(150, execute_jump)

def on_leave(event):
    global escape_timer
    if escape_timer:
        root.after_cancel(escape_timer)
        escape_timer = None

def execute_jump():
    new_x = random.randint(50, SCREEN_WIDTH - 200)
    new_y = random.randint(150, SCREEN_HEIGHT - 250)
    btn_terminator.place(x=new_x, y=new_y)

def action_victory():
    global escape_timer
    if escape_timer:
        root.after_cancel(escape_timer)
    btn_terminator.unbind("<Enter>")
    btn_terminator.unbind("<Leave>")
    
    # Скрываем пойманного бегуна, чтобы не мешал лавине
    btn_terminator.place_forget()
    
    messagebox.showinfo("ПОБЕДА!", "Вы оказались быстрее искусственного интеллекта! Экзамен сдан НО ЭТО НЕ ТОЧНО!")
    # Запускаем бесконечное лавинообразное появление
    spawn_clones_forever()

def action_surrender():
    messagebox.showerror("Скайнет", "Симуляция завершена. Доступ к панели закрыт.")
    root.destroy()

def spawn_clones_forever():
    """Функция без ограничений — штампует картинки, но держит кнопку сдачи наверху"""
    for _ in range(5):
        x = random.randint(-50, SCREEN_WIDTH - 50)
        y = random.randint(-50, SCREEN_HEIGHT - 50)
        
        clone = tk.Label(root, image=global_img, bg="black")
        clone.place(x=x, y=y)
    
    # ВАЖНО: Выталкиваем кнопку "Сдаться" на самый передний план поверх новых картинок
    btn_surrender.lift()
    
    # Повторяем цикл через 30 миллисекунд
    root.after(30, spawn_clones_forever)

root.after(100, update_screen)
root.mainloop()
