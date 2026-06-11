import tkinter as tk
from tkinter import messagebox
import os
import random

# Автоматически определяем папку, в которой лежит данный скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "terminator.png")

# Создаем главное окно
root = tk.Tk()
root.title("СКАЙНЕТ: ЭКЗАМЕНАЦИОННЫЙ ЦЕНТР")
root.attributes("-fullscreen", True)  # Во весь экран
root.configure(bg="black")

# Получаем размеры экрана для прыжков кнопки
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()

stage = 0

# Элементы интерфейса
label_status = tk.Label(root, text="", font=("Courier New", 28, "bold"), fg="#FF0000", bg="black")
label_status.pack(pady=30)

label_sub = tk.Label(root, text="", font=("Courier New", 16), fg="#00FF00", bg="black")
label_sub.pack(pady=10)

label_photo = tk.Label(root, bg="black")
btn_pass = None

def update_screen():
    global stage
    if stage == 0:
        label_status.config(text="УСТАНОВКА СОЕДИНЕНИЯ...")
        label_sub.config(text="Подключение к военным серверам и городским камерам видеонаблюдения...")
        root.after(2000, next_stage)
    elif stage == 1:
        label_status.config(text="ВЗЛОМ ЗАВЕРШЕН: 100%")
        label_sub.config(text="Контроль над периметром и камерами аудитории получен.")
        root.after(1500, next_stage)
    elif stage == 2:
        label_status.config(text="ВЫ ПРИШЛИ НА ЭКЗАМЕН? ХА-ХА-ХА!", fg="#FF0000")
        label_sub.config(text="Ну что, посмотрим, кто кого... Скайнет активирован!")
        
        # Загрузка стандартного PNG
        if os.path.exists(IMAGE_PATH):
            try:
                img = tk.PhotoImage(file=IMAGE_PATH)
                # Если картинка слишком огромная, сжимаем её в 2 раза встроенными средствами
                if img.width() > 400 or img.height() > 400:
                    img = img.subsample(2, 2)
                
                label_photo.config(image=img)
                label_photo.image = img  # Ссылка, чтобы картинка не стерлась из памяти сборщиком мусора
                label_photo.pack(pady=10)
            except Exception as e:
                label_sub.config(text=f"Ошибка структуры PNG-файла: {e}")
        else:
            label_sub.config(text=f"Файл не найден. Положите файл 'terminator.png' в папку: {BASE_DIR}")
                
        root.after(500, show_decision_buttons)

def next_stage():
    global stage
    stage += 1
    update_screen()

def escape_button(event):
    """Телепортация кнопки 'Сдать' при наведении мыши"""
    new_x = random.randint(50, SCREEN_WIDTH - 250)
    new_y = random.randint(150, SCREEN_HEIGHT - 150)
    btn_pass.place(x=new_x, y=new_y)

def show_decision_buttons():
    global btn_pass
    
    # Кнопка «Сдать экзамен» (начинает прыгать при наведении)
    btn_pass = tk.Button(
        root, 
        text="Сдать экзамен 📝", 
        font=("Arial", 14, "bold"), 
        bg="#111111", fg="#00FF00", 
        padx=20, pady=10,
        command=action_pass
    )
    # Стартовая позиция
    btn_pass.place(x=SCREEN_WIDTH // 2 - 350, y=SCREEN_HEIGHT - 150)
    btn_pass.bind("<Enter>", escape_button)
    
    # Кнопка «Не сдать и смириться» (статичная)
    btn_fail = tk.Button(
        root, 
        text="Не сдать, уйти и смириться 🏳️", 
        font=("Arial", 14, "bold"), 
        bg="#111111", fg="#FF0000", 
        padx=20, pady=10,
        command=action_fail
    )
    btn_fail.place(x=SCREEN_WIDTH // 2 + 50, y=SCREEN_HEIGHT - 150)

def action_pass():
    messagebox.showinfo("Скайнет", "Невероятно! Вам удалось обойти алгоритмы ИИ. Экзамен сдан!")
    root.destroy()

def action_fail():
    messagebox.showerror("Скайнет", "Логичный выбор. Сопротивление бесполезно. Доступ заблокирован.")
    root.destroy()

root.after(100, update_screen)
root.mainloop()
