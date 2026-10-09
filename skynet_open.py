import tkinter as tk
import customtkinter as ctk
import sys
import os
from PIL import Image, ImageTk

# Настройки окна (темная тема)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # Исправлено здесь

# Путь к вашей GIF-анимации
GIF_PATH = "skynet.gif"

class SkynetApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Разворачиваем окно на весь экран
        self.attributes("-fullscreen", True)
        self.configure(fg_color="#0a0a0a")
        
        # Контейнер для центрирования элементов
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Главный текст
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="ВНИМАНИЕ: СИСТЕМА ЗАРАЖЕНА ВИРУСОМ SKYNET", 
            font=("Arial", 28, "bold"),
            text_color="#ff3333"
        )
        self.title_label.pack(pady=10)

        # Подтекст
        self.subtitle_label = ctk.CTkLabel(
            self.main_frame, 
            text="И я это докажу прямо сейчас...", 
            font=("Arial", 18),
            text_color="#ffffff"
        )
        self.subtitle_label.pack(pady=10)

        # Контейнер для GIF
        self.gif_label = tk.Label(self.main_frame, bg="#0a0a0a")
        self.gif_label.pack(pady=20)
        
        # Загрузка и запуск GIF
        self.load_gif()

        # Кнопка "Принять и продолжить"
        self.action_button = ctk.CTkButton(
            self.main_frame, 
            text="Принять и продолжить", 
            font=("Arial", 16, "bold"),
            fg_color="#ff3333",
            hover_color="#cc0000",
            text_color="white",
            height=45,
            command=self.trigger_action
        )
        self.action_button.pack(pady=20)

        # Аварийный выход для вас по клавише Escape
        self.bind("<Escape>", lambda e: self.close_program())

    def load_gif(self):
        """Загружает GIF и подготавливает кадры для анимации"""
        if os.path.exists(GIF_PATH):
            self.gif_image = Image.open(GIF_PATH)
            self.frames = []
            
            try:
                while True:
                    # Копируем кадр, изменяем размер и добавляем в список
                    frame = self.gif_image.copy().convert("RGBA")
                    frame = frame.resize((400, 300), Image.Resampling.LANCZOS)
                    self.frames.append(ImageTk.PhotoImage(frame))
                    self.gif_image.seek(len(self.frames))  # Переходим к следующему кадру
            except EOFError:
                pass  # Конец кадров в GIF

            self.frame_index = 0
            self.animate_gif()
        else:
            # Если гифки нет, просто покажем заглушку
            self.gif_label.configure(text="[ АНИМАЦИЯ SKYNET ]", font=("Arial", 24), fg="white")

    def animate_gif(self):
        """Циклически воспроизводит кадры GIF"""
        if self.frames:
            frame = self.frames[self.frame_index]
            self.gif_label.configure(image=frame)
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            # Скорость анимации (100 мс между кадрами)
            self.after(100, self.animate_gif)

    def trigger_action(self):
        """Открывает CD-ROM и закрывает программу"""
        # Запуск команды открытия дисковода через PowerShell из Python
        cmd = 'powershell -command "(New-Object -ComObject WMPlayer.OCX.7).cdromCollection.Item(0).Eject()"'
        os.system(cmd)
        
        # Небольшая пауза, чтобы дисковод успел выехать до закрытия окна
        self.after(1000, self.close_program)

    def close_program(self):
        self.destroy()
        sys.exit()

if __name__ == "__main__":
    app = SkynetApp()
    app.mainloop()
