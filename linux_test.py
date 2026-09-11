import tkinter as tk
from tkinter import messagebox
import time

# Список вопросов: (Вопрос, [Варианты], Индекс правильного ответа)
QUESTIONS = [
    ("Что делает команда grep?", ["Копирует файлы", "Ищет текст по шаблону", "Удаляет директории", "Перезагружает ПК"], 1),
    ("Для чего нужна команда cat?", ["Выводит содержимое файла", "Создает пользователя", "Показывает котиков", "Форматирует диск"], 0),
    ("Что означает команда sudo?", ["Удалить всё", "Запустить от имени суперпользователя", "Скачать файл", "Выйти из системы"], 1),
    ("Какая команда показывает текущую директорию?", ["pwd", "ls", "cd", "whereami"], 0),
    ("Как посмотреть список файлов в папке?", ["dir /w", "show", "ls", "list"], 2),
    ("Какая команда создает новую папку?", ["mkdir", "newdir", "create", "touch"], 0),
    ("Как создать пустой файл?", ["cat", "touch", "nano", "echo"], 1),
    ("Какая команда используется для смены прав доступа к файлу?", ["chown", "chmod", "rights", "sudo"], 1),
    ("Как завершить процесс по его ID?", ["stop", "end", "kill", "close"], 2),
    ("Какая команда выводит мануал (справку) по другой команде?", ["help", "info", "man", "guide"], 2)
]

class LinuxQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Core Verification System")
        
        # БЛОКИРОВКА: Раскрываем на весь экран и поверх всех окон
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", True)
        self.root.config(bg="#1e1e1e")
        
        self.score = 0
        self.current_q = 0
        self.student_name = ""

        # Шапка с Линусом Торвальдсом (всегда на экране)
        self.header_frame = tk.Frame(self.root, bg="#2d2d2d", bd=2, relief="solid")
        self.header_frame.pack(fill="x", side="top", ipady=10)
        
        try:
            self.img = tk.PhotoImage(file="torvalds.png")
            # Если фото слишком большое, можно уменьшить его масштаб (например, в 2 раза):
            # self.img = self.img.subsample(2, 2)
            self.img_label = tk.Label(self.header_frame, image=self.img, bg="#2d2d2d")
            self.img_label.pack(side="left", padx=20)
        except Exception:
            # На случай, если картинки нет рядом
            self.img_label = tk.Label(self.header_frame, text="[Фото Торвальдса]", fg="white", bg="red", font=("Arial", 14))
            self.img_label.pack(side="left", padx=20)

        self.torvalds_text = tk.Label(
            self.header_frame, 
            text="Привет! Меня зовут Линус Торвальдс.\nЯ хочу проверить твои знания по ОС Linux.", 
            fg="#00ff00", bg="#2d2d2d", font=("Courier New", 18, "bold"), justify="left"
        )
        self.torvalds_text.pack(side="left", padx=20)

        # Главная рабочая область под шапкой
        self.main_frame = tk.Frame(self.root, bg="#1e1e1e")
        self.main_frame.pack(expand=True, fill="both", pady=20)

        # Запуск первого этапа — знакомство
        self.start_intro()

    def start_intro(self):
        # Форма ввода имени
        self.clear_frame()
        
        lbl = tk.Label(self.main_frame, text="Представься, студент (Введи имя):", fg="white", bg="#1e1e1e", font=("Arial", 16))
        lbl.pack(pady=20)
        
        self.name_entry = tk.Entry(self.main_frame, font=("Arial", 16), width=30, justify="center")
        self.name_entry.pack(pady=10)
        self.name_entry.focus_set()
        
        btn = tk.Button(self.main_frame, text="Войти в систему", font=("Arial", 14), command=self.scan_brain_animation, bg="#4CAF50", fg="white")
        btn.pack(pady=20)

    def scan_brain_animation(self):
        self.student_name = self.name_entry.get().strip()
        if not self.student_name:
            messagebox.showwarning("Эй!", "Анонимов в ядро Linux не пускаем! Введи имя.")
            return
            
        self.clear_frame()
        
        # Меняем текст Торвальдса
        self.torvalds_text.config(text=f"Приветствую, {self.student_name}!\nИнициализирую проверку системы...")
        
        self.scan_label = tk.Label(self.main_frame, text="", fg="yellow", bg="#1e1e1e", font=("Courier New", 16, "bold"), justify="center")
        self.scan_label.pack(expand=True)
        
        # Шуточная цепочка анимации сканирования
        self.root.after(1000, lambda: self.scan_label.config(text="Запуск процесса: Идет сканирование головного мозга..."))
        self.root.after(3000, lambda: self.scan_label.config(text="Результат: Найдена ОДНА извилина! 🧠\n(Но это не точно...)"))
        self.root.after(5500, lambda: self.scan_label.config(text="Ой... Секунду...\n[КРИТИЧЕСКАЯ ОШИБКА СКАНЕРА]"))
        self.root.after(7500, lambda: self.scan_label.config(text="А, нет, всё в порядке!\nНайдено ДВЕ извилины! Значит, не всё потеряно. 👍"))
        self.root.after(10500, self.start_quiz)

    def start_quiz(self):
        self.torvalds_text.config(text=f"Студент: {self.student_name}\nОтвечай на вопросы честно. Я слежу.")
        self.show_question()

    def show_question(self):
        self.clear_frame()
        
        if self.current_q >= len(QUESTIONS):
            self.show_results()
            return
            
        q_text, options, _ = QUESTIONS[self.current_q]
        
        # Номер вопроса
        q_num_lbl = tk.Label(self.main_frame, text=f"Вопрос {self.current_q + 1} из {len(QUESTIONS)}", fg="#888888", bg="#1e1e1e", font=("Arial", 12))
        q_num_lbl.pack(pady=5)
        
        # Текст вопроса
        q_lbl = tk.Label(self.main_frame, text=q_text, fg="white", bg="#1e1e1e", font=("Arial", 20, "bold"), wrap=800)
        q_lbl.pack(pady=20)
        
        # Переменная для хранения выбора
        self.var = tk.IntVar(value=-1)
        
        # Кнопки вариантов ответов
        for i, option in enumerate(options):
            rb = tk.Radiobutton(
                self.main_frame, text=option, variable=self.var, value=i,
                fg="white", bg="#1e1e1e", selectcolor="#2d2d2d",
                activebackground="#1e1e1e", activeforeground="white",
                font=("Arial", 14), anchor="w", width=40, padx=20, pady=5
            )
            rb.pack(pady=5)
            
        # Кнопка Дальше
        next_btn = tk.Button(self.main_frame, text="Ответить", font=("Arial", 14, "bold"), command=self.check_answer, bg="#008CBA", fg="white", width=15)
        next_btn.pack(pady=30)

    def check_answer(self):
        if self.var.get() == -1:
            messagebox.showwarning("Внимание", "Выберите один из вариантов ответа!")
            return
            
        _, _, correct_idx = QUESTIONS[self.current_q]
        if self.var.get() == correct_idx:
            self.score += 1
            
        self.current_q += 1
        self.show_question()

    def show_results(self):
        self.clear_frame()
        self.torvalds_text.config(text=f"Тестирование завершено.\n{self.student_name}, смотрим твои результаты...")
        
        total = len(QUESTIONS)
        percent = (self.score / total) * 100
        
        # Шкала результатов (визуальная полоса)
        scale_bg = tk.Frame(self.main_frame, bg="#333333", width=400, height=25)
        scale_bg.pack(pady=20)
        scale_bg.pack_propagate(False)
        
        scale_fill = tk.Frame(scale_bg, bg="#00ff00" if percent >= 70 else "yellow" if percent >= 40 else "red", width=int(4 * percent), height=25)
        scale_fill.pack(side="left")
        
        # Текст уровня
        res_lbl = tk.Label(self.main_frame, text=f"Правильных ответов: {self.score} из {total} ({percent:.0f}%)", fg="white", bg="#1e1e1e", font=("Arial", 18, "bold"))
        res_lbl.pack(pady=10)
        
        # Подведение итогов по вашему сценарию
        if self.score >= 8:
            verdict = "Уровень: ГУРУ БАША 😎\n\nВсё хорошо, парень! Ты не зря ковырялся в терминале. Одобряю!"
            verdict_color = "#00ff00"
        elif self.score >= 4:
            verdict = "Уровень: ПОЛУ-ПИНГВИН 🐧\n\nНу, средне. Поучись еще, парень, не всё еще потеряно!"
            verdict_color = "yellow"
        else:
            verdict = "Уровень: КРЕПКИЙ ОКОННЫЙ ЖИТЕЛЬ 🪟\n\nКупи книжку для начала 'Windows для чайников', а потом звони мне — что-нибудь решим."
            verdict_color = "#ff4444"
            
        verdict_lbl = tk.Label(self.main_frame, text=verdict, fg=verdict_color, bg="#1e1e1e", font=("Arial", 16, "bold"), justify="center", wrap=600)
        verdict_lbl.pack(pady=20)
        
        # Кнопка выхода (разблокировки)
        exit_btn = tk.Button(self.main_frame, text="Закрыть терминал", font=("Arial", 14), command=self.root.destroy, bg="#f44336", fg="white")
        exit_btn.pack(pady=20)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LinuxQuizApp(root)
    root.mainloop()
