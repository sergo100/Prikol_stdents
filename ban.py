import tkinter as tk
import sys

# Создание главного окна
root = tk.Tk()
root.title("Система блокировки")

# Развернуть окно на весь экран
root.attributes('-fullscreen', True)
root.configure(bg='#1a1a1a')  # Темный фон

# Главный контейнер для центрирования всех элементов
frame = tk.Frame(root, bg='#1a1a1a')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Крупный текст "БАН ЗА ЧИТЕРСТВО"
ban_label = tk.Label(
    frame, 
    text="БАН ЗА ЧИТЕРСТВО", 
    font=("Arial", 48, "bold"), 
    fg="#ff3333",  # Ярко-красный цвет
    bg="#1a1a1a"
)
ban_label.pack(pady=20)

# Пояснительный текст
desc_label = tk.Label(
    frame, 
    text="Использование стороннего ПО во время тестирования строго запрещено.", 
    font=("Arial", 16), 
    fg="#ffffff", 
    bg="#1a1a1a"
)
desc_label.pack(pady=15)

# Функция для закрытия программы
def close_program():
    root.destroy()
    sys.exit()

# Контейнер для кнопок, чтобы расположить их в один ряд
buttons_frame = tk.Frame(frame, bg='#1a1a1a')
buttons_frame.pack(pady=30)

# Кнопка "ПРИНЯТЬ"
accept_button = tk.Button(
    buttons_frame, 
    text="ПРИНЯТЬ", 
    command=close_program, 
    font=("Arial", 14, "bold"), 
    bg="#ff3333", 
    fg="white", 
    activebackground="#cc0000", 
    activeforeground="white", 
    padx=30, 
    pady=10, 
    bd=0, 
    cursor="hand2"
)
accept_button.pack(side=tk.LEFT, padx=15)  # side=tk.LEFT ставит в ряд

# Кнопка "ПОНЯТЬ"
understand_button = tk.Button(
    buttons_frame, 
    text="ПОНЯТЬ", 
    command=close_program, 
    font=("Arial", 14, "bold"), 
    bg="#444444", 
    fg="white", 
    activebackground="#333333", 
    activeforeground="white", 
    padx=30, 
    pady=10, 
    bd=0, 
    cursor="hand2"
)
understand_button.pack(side=tk.LEFT, padx=15)

# Кнопка "Прийти на пересдачу"
understand_button = tk.Button(
    buttons_frame, 
    text="Прийти на пересдачу", 
    command=close_program, 
    font=("Arial", 14, "bold"), 
    bg="#0A9146", 
    fg="white", 
    activebackground="#2C1FA1", 
    activeforeground="white", 
    padx=30, 
    pady=10, 
    bd=0, 
    cursor="hand2"
)
understand_button.pack(side=tk.BOTTOM, padx=15)

# Запуск отображения окна
root.mainloop()
