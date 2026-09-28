import tkinter as tk
import sys
import os
from PIL import Image, ImageTk

# Укажите путь к вашей страшной картинке
# Положите файл в ту же папку, где лежит этот скрипт
SCREAMER_IMAGE_PATH = "screamer.png" 

# Создание главного окна
root = tk.Tk()
root.title("Система блокировки")

# Развернуть окно на весь экран
root.attributes("-fullscreen", True)
root.configure(bg="#1a1a1a")  # Темный фон

# Главный контейнер для центрирования всех элементов
frame = tk.Frame(root, bg="#1a1a1a")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Функция, которая активирует скример при нажатии на кнопку
def trigger_screamer():
    # 1. Удаляем текст и кнопки с экрана
    frame.destroy()
    
    # 2. Выводим картинку скримера на весь экран
    if os.path.exists(SCREAMER_IMAGE_PATH):
        # Получаем размеры текущего экрана
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Открываем изображение и растягиваем под размер монитора
        img = Image.open(SCREAMER_IMAGE_PATH)
        img = img.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        
        # Сохраняем ссылку в global, чтобы картинка не исчезла из памяти
        global photo
        photo = ImageTk.PhotoImage(img)
        
        # Создаем слой для картинки
        screamer_label = tk.Label(root, image=photo, bg="black")
        screamer_label.pack(fill="both", expand=True)
    else:
        # Запасной вариант, если файла картинки нет в папке
        root.configure(bg="#ff0000")
        fail_label = tk.Label(root, text="БУ!", font=("Arial", 96, "bold"), fg="black", bg="#ff0000")
        fail_label.place(relx=0.5, rely=0.5, anchor="center")

    # 3. Закрываем программу автоматически через 3 секунды
    root.after(3000, close_program)

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