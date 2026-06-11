import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Система Скайнет: Внимание")
root.attributes("-fullscreen", True)  # Разворачиваем на весь экран
root.configure(bg="black")            # Черный хакерский фон

# Красный пугающий заголовок
label_title = tk.Label(
    root, 
    text="ПОПАЛИСЬ! ХА-ХА-ХА", 
    font=("Courier New", 36, "bold"), 
    fg="#FF0000", 
    bg="black"
)
label_title.pack(pady=30)

# Текст сообщения системы
message_text = (
    "СИСТЕМА СКАЙНЕТ АКТИВИРОВАНА\n"
    "ВСЕ ВАШИ ДАННЫЕ УНИЧТОЖЕНЫ...\n"
    "ЭКЗАМЕН ЗАФЕЙЛЕН!"
)
label_msg = tk.Label(
    root, 
    text=message_text, 
    font=("Courier New", 20, "bold"), 
    fg="#00FF00",  # Зеленый цвет терминала
    bg="black",
    justify="center"
)
label_msg.pack(pady=20)

# Рисунок Терминатора из символов (ASCII-арт)
terminator_ascii = """
      .---.
     /     \\
     \\_.._/
     ||  ||    [ СКАЙНЕТ МОДЕРН-I ]
     ||__||   
    /   __   \\   _______

   | .-'  '-. | |       |
   |/  (o)(o)  \\|       |
   |   .---.   |        |
    \\  |||||  /________/
     '. '---' .'
       '-...-'
"""

label_art = tk.Label(
    root, 
    text=terminator_ascii, 
    font=("Consolas", 14), 
    fg="#33FFF3",  # Неоновый голубой
    bg="black",
    justify="left"
)
label_art.pack(pady=20)

# Кнопка для закрытия шуточного окна
btn_exit = tk.Button(
    root, 
    text="Принять поражение и выйти", 
    font=("Arial", 12), 
    command=root.destroy, 
    bg="#333333", 
    fg="white", 
    relief="flat"
)
btn_exit.pack(side="bottom", pady=50)

# Запуск окна
root.mainloop()