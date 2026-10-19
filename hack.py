import tkinter as tk
import random

# Исходный текст и настройки
GLITCH_CHARS = ["@", "#", "$", "%", "&", "*", "0", "1", "X", "Ø", " ERROR "]
COUNTDOWN_TIME = 5  # Время таймера в секундах

def on_closing():
    """Запрещает закрытие окна и переносит его в случайное место"""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Случайные координаты, чтобы окно не улетело за экран
    new_x = random.randint(100, screen_width - 500)
    new_y = random.randint(100, screen_height - 300)
    root.geometry(f"+{new_x}+{new_y}")

def start_countdown(seconds):
    """Функция таймера обратного отсчета"""
    if seconds > 0:
        lbl_text.config(text=f"ВНИМАНИЕ! ОБНАРУЖЕН ВЗЛОМ!\n\nДо полной блокировки системы:\n{seconds} сек.")
        root.after(1000, start_countdown, seconds - 1)
    else:
        # Переходим к разрушению интерфейса
        crash_effect()

def crash_effect():
    """Эффект разрушения текста и дрожания окна"""
    current_text = lbl_text.cget("text")
    
    # Если остались обычные символы, продолжаем ломать текст
    if any(c not in GLITCH_CHARS and c != "\n" for c in current_text):
        text_list = list(current_text)
        # Заменяем по 4 символа за раз для более агрессивного эффекта
        for _ in range(4):
            idx = random.randint(0, len(text_list) - 1)
            if text_list[idx] != "\n":
                text_list[idx] = random.choice(GLITCH_CHARS)
        
        lbl_text.config(text="".join(text_list))
        
        # Сильное дрожание окна
        x = root.winfo_x() + random.randint(-6, 6)
        y = root.winfo_y() + random.randint(-6, 6)
        root.geometry(f"+{x}+{y}")
        
        root.after(60, crash_effect)
    else:
        # Финальный экран падения
        lbl_text.config(text="SYSTEM FAILURE\n\n[CORE DUMPED]\nACCESS DENIED", fg="lime")
        root.configure(bg="black")
        lbl_text.configure(bg="black")

# Инициализация окна
root = tk.Tk()
root.title("System Warning")
root.geometry("450x220")
root.resizable(False, False)

# Перехватываем нажатие на системный крестик [X]
root.protocol("WM_DELETE_WINDOW", on_closing)

# Центрируем окно при первом запуске
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
start_x = (screen_width // 2) - (450 // 2)
start_y = (screen_height // 2) - (220 // 2)
root.geometry(f"+{start_x}+{start_y}")

root.configure(bg="#f0f0f0")

# Создаем текстовое поле
lbl_text = tk.Label(
    root, 
    text="", 
    font=("Courier New", 12, "bold"), 
    fg="red", 
    bg="#f0f0f0",
    justify="center"
)
lbl_text.pack(expand=True, fill="both", pady=20)

# Запускаем обратный отсчет
start_countdown(COUNTDOWN_TIME)

root.mainloop()
