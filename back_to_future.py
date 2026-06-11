import os
import tkinter as tk
from tkinter import messagebox

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


QUESTIONS = [
    {
        "question": "Как зовут главного героя фильма?",
        "answers": [
            "Марти Макфлай",
            "Джордж Макфлай",
            "Бифф Таннен",
            "Эмметт Браун"
        ],
        "correct": 0
    },
    {
        "question": "Как назывался автомобиль времени?",
        "answers": [
            "Ford Mustang",
            "DeLorean",
            "Chevrolet Camaro",
            "Tesla"
        ],
        "correct": 1
    },
    {
        "question": "Сколько энергии требовалось машине времени?",
        "answers": [
            "121 МВт",
            "1.21 ГВт",
            "12.1 ГВт",
            "21 ГВт"
        ],
        "correct": 1
    },
    {
        "question": "К кому обратиться за помощью?",
        "answers": [
            "Я гуль",
            "Помощь друга",
            "Сикс севен"
        ],
        "special": True
    },
    {
        "question": "Кто был главным антагонистом первой части?",
        "answers": [
            "Бифф Таннен",
            "Док Браун",
            "Марти Макфлай",
            "Эйнштейн"
        ],
        "correct": 0
    }
]


class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Временная аномалия")
        self.root.attributes("-fullscreen", True)

        self.index = -1

        self.frame = tk.Frame(
            root,
            bg="black"
        )
        self.frame.pack(
            fill="both",
            expand=True
        )

        # Вызываем загрузку картинки перед созданием виджета
        self.load_image()

        self.image_label = tk.Label(
            self.frame,
            bg="black"
        )
        self.image_label.pack(
            pady=10
        )

        # Если картинка успешно считалась — привязываем её к Label
        if self.photo:
            self.image_label.config(
                image=self.photo
            )

        self.title_label = tk.Label(
            self.frame,
            text="⚠ ВРЕМЕННАЯ АНОМАЛИЯ ОБНАРУЖЕНА ⚠",
            font=("Consolas", 24, "bold"),
            fg="lime",
            bg="black"
        )
        self.title_label.pack(
            pady=10
        )

        self.text_label = tk.Label(
            self.frame,
            text=(
                "Обнаружено подключение к 1985 году.\n"
                "Проверка временной линии...\n"
                "Для продолжения пройдите проверку."
            ),
            font=("Consolas", 16),
            fg="lime",
            bg="black",
            justify="center"
        )
        self.text_label.pack(
            pady=10
        )

        self.answers_frame = tk.Frame(
            self.frame,
            bg="black"
        )
        self.answers_frame.pack(
            pady=10
        )

        self.start_btn = tk.Button(
            self.frame,
            text="Начать проверку",
            command=self.next_question,
            font=("Consolas", 14)
        )
        self.start_btn.pack(
            pady=10
        )

        self.exit_btn = tk.Button(
            self.frame,
            text="Выйти",
            command=self.root.destroy,
            font=("Consolas", 12)
        )
        self.exit_btn.pack(
            pady=10
        )

        self.root.bind(
            "<Escape>",
            lambda e: self.root.destroy()
        )

    def load_image(self):
        self.photo = None
        img_filename = "back_to_future.jpg"

        if not PIL_AVAILABLE:
            print("❌ Ошибка: Библиотека Pillow (PIL) не установлена в системе.")
            return

        # Проверяем физическое наличие файла на диске
        if not os.path.exists(img_filename):
            print(f"❌ Ошибка: Файл '{img_filename}' не найден в текущей папке скрипта!")
            print(f"📂 Текущая папка поиска: {os.getcwd()}")
            return

        try:
            # Открываем изображение безопасным способом
            with Image.open(img_filename) as img:
                img.thumbnail((700, 450))
                # Переводим в формат, понятный для Tkinter
                self.photo = ImageTk.PhotoImage(img)
                print(f"✅ Картинка '{img_filename}' успешно загружена.")
        except Exception as e:
            print(f"❌ Ошибка при чтении изображения через PIL: {e}")

    def clear_answers(self):
        for widget in self.answers_frame.winfo_children():
            widget.destroy()

    def next_question(self):
        self.index += 1

        if self.index >= len(QUESTIONS):
            self.finish()
            return

        self.show_question()

    def show_question(self):
        self.start_btn.pack_forget()
        self.clear_answers()

        q = QUESTIONS[self.index]

        self.title_label.config(
            text=f"Уровень {self.index + 1} из 5"
        )

        self.text_label.config(
            text=q["question"]
        )

        for i, answer in enumerate(q["answers"]):
            btn = tk.Button(
                self.answers_frame,
                text=answer,
                width=40,
                font=("Consolas", 12),
                command=lambda x=i: self.check_answer(x)
            )
            btn.pack(
                pady=5
            )

    def check_answer(self, choice):
        q = QUESTIONS[self.index]

        if q.get("special"):
            if choice == 1:
                messagebox.showinfo(
                    "Помошь друга",
                    "Подключаемся к другу...\n"
                    "Совет получен. Вы назначены адмимнистратором сети. ИИ Победил\n"
                    "Доступ разрешён."
                )
                self.next_question()
            else:
                messagebox.showwarning(
                    "Ошибка",
                    "Временная линия нестабильна.\n"
                    "Попробуйте ещё раз."
                )
            return

        if choice == q["correct"]:
            self.next_question()
        else:
            messagebox.showwarning(
                "Ошибка",
                "Неверный ответ."
            )

    def finish(self):
        self.clear_answers()

        self.title_label.config(
            text="✓ ВРЕМЕННАЯ ЛИНИЯ ВОССТАНОВЛЕНА"
        )

        self.text_label.config(
            text=(
                "Компьютер не взломан.\n"
                "Камеры загружаются.\n"
                "Данные защищены.\n\n"
                "Теперь можно сдавать экзамен!"
            )
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = Quiz(root)
    root.mainloop()
