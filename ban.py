import tkinter as tk
import sys
import os
from PIL import Image, ImageTk

# Настройки путей к файлам (положите картинку скримера в папку со скриптом)
SCREAMER_IMAGE_PATH = "screamer.png"

# Создание главного окна
root = tk.Tk()
root.title("Система блокировки")

# Развернуть окно на весь экран
root.attributes("-fullscreen", True)
root.configure(bg="#1a1a1a")  # Темный фон

# Главный контейнер для центрирования всех элементов начального экрана
frame = tk.Frame(root, bg="#1a1a1a")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Глобальная переменная для управления слоем экрана розыгрыша
current_screamer_layer = None

# Функция, которая активирует скример при нажатии на любую кнопку
def trigger_screamer():
    global current_screamer_layer
    
    # 1. Полностью удаляем текст и кнопки начального экрана
    frame.destroy()
    
    # 2. Выводим картинку скримера на весь экран
    if os.path.exists(SCREAMER_IMAGE_PATH):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        img = Image.open(SCREAMER_IMAGE_PATH)
        img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        
        global photo_screamer
        photo_screamer = ImageTk.PhotoImage(img)
        
        current_screamer_layer = tk.Label(root, image=photo_screamer, bg="black")
        current_screamer_layer.pack(fill="both", expand=True)
    else:
        # Запасной текстовый вариант, если картинки скримера нет
        current_screamer_layer = tk.Label(root, text="БУ!", font=("Arial", 96, "bold"), fg="black", bg="#ff0000")
        current_screamer_layer.pack(fill="both", expand=True)

    # 3. Через 2 секунды (2000 мс) убираем скример и показываем мем
    root.after(2000, trigger_robert_weide)

# Функция, которая выводит текстовый мем на экран
def trigger_robert_weide():
    global current_screamer_layer
    
    # Уничтожаем слой со скримером
    if current_screamer_layer:
        current_screamer_layer.destroy()
        
    # Делаем фон главного окна глубоким черным
    root.configure(bg="black")
    
    # Создаем контейнер для титров мема ровно по центру экрана
    meme_frame = tk.Frame(root, bg="black")
    meme_frame.place(relx=0.5, rely=0.5, anchor="center")
    
    # Верхняя строчка оригинального мема
    directed_label = tk.Label(
        meme_frame, 
        text="DIRECTED BY", 
        font=("Times New Roman", 34),  # Использован более классический шрифт для кинотитров
        fg="white", 
        bg="black"
    )
    directed_label.pack(pady=10)
    
    # Нижняя строчка оригинального мема
    name_label = tk.Label(
        meme_frame, 
        text="ROBERT B. WEIDE", 
        font=("Times New Roman", 48, "bold"), 
        fg="white", 
        bg="black"
    )
    name_label.pack(pady=10)
    
    # 4. Держим мем на экране 4 секунды (4000 мс) и затем закрываем программу
    root.after(4000, close_program)

# Функция для закрытия программы
def close_program():
    root.destroy()
    sys.exit()

# Закрытие программы по нажатию на клавишу Escape (Esc) для экстренного выхода
root.bind("<Escape>", lambda event: close_program())

# Крупный текст БАН ЗА ЧИТЕРСТВО
ban_label = tk.Label(frame, text="БАН ЗА ЧИТЕРСТВО", font=("Arial", 48, "bold"), fg="#ff3333", bg="#1a1a1a")
ban_label.pack(pady=20)

# Пояснительный текст
desc_label = tk.Label(frame, text="Использование стороннего ПО во время тестирования строго запрещено.", font=("Arial", 16), fg="#ffffff", bg="#1a1a1a")
desc_label.pack(pady=15)

# Контейнер для кнопок
buttons_frame = tk.Frame(frame, bg="#1a1a1a")
buttons_frame.pack(pady=30)

# Кнопка ПРИНЯТЬ
accept_button = tk.Button(buttons_frame, text="ПРИНЯТЬ", command=trigger_screamer, font=("Arial", 14, "bold"), bg="#ff3333", fg="white", activebackground="#cc0000", activeforeground="white", padx=30, pady=10, bd=0, cursor="hand2")
accept_button.pack(side=tk.LEFT, padx=15)

# Кнопка ПОНЯТЬ
understand_button = tk.Button(buttons_frame, text="ПОНЯТЬ", command=trigger_screamer, font=("Arial", 14, "bold"), bg="#444444", fg="white", activebackground="#333333", activeforeground="white", padx=30, pady=10, bd=0, cursor="hand2")
understand_button.pack(side=tk.LEFT, padx=15)

# Кнопка Прийти на пересдачу
retake_button = tk.Button(buttons_frame, text="Прийти на пересдачу", command=trigger_screamer, font=("Arial", 14, "bold"), bg="#0A9146", fg="white", activebackground="#087337", activeforeground="white", padx=30, pady=10, bd=0, cursor="hand2")
retake_button.pack(side=tk.LEFT, padx=15)

# Запуск основного цикла программы
root.mainloop()
