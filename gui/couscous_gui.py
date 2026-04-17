"""
🍝 Кускус-визуализатор - GUI приложение
Запуск: python gui/couscous_gui.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

# Добавляем родительскую папку в путь для импорта
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from symmetrical_couscous import *

class CouscousApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🍝 Симметричный кускус - Визуализатор")
        self.root.geometry("600x500")
        self.root.configure(bg='#fff8e7')
        
        # Заголовок
        title = tk.Label(root, text="🍝 Симметричный кускус 🍚", 
                         font=("Arial", 20, "bold"), bg='#fff8e7', fg='#d2691e')
        title.pack(pady=20)
        
        # Поле ввода
        input_frame = tk.Frame(root, bg='#fff8e7')
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Введите массив (через запятую):", 
                bg='#fff8e7', font=("Arial", 12)).pack()
        
        self.entry = tk.Entry(input_frame, width=50, font=("Arial", 12))
        self.entry.pack(pady=5)
        self.entry.insert(0, "1,2,3,4,5,6,7,8")
        
        # Выбор алгоритма
        tk.Label(root, text="Выберите алгоритм:", bg='#fff8e7', font=("Arial", 12)).pack()
        
        self.algo_var = tk.StringVar(value="Симметричный")
        algorithms = ["Симметричный", "Хаотичный", "Золотой", "Фрактальный", "Спиральный"]
        
        algo_frame = tk.Frame(root, bg='#fff8e7')
        algo_frame.pack(pady=5)
        
        for algo in algorithms:
            tk.Radiobutton(algo_frame, text=algo, variable=self.algo_var, 
                          value=algo, bg='#fff8e7', font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        
        # Кнопка
        self.button = tk.Button(root, text="🍝 Приготовить кускус!", 
                               command=self.process, bg='#d2691e', fg='white',
                               font=("Arial", 14, "bold"), padx=20, pady=10)
        self.button.pack(pady=20)
        
        # Результат
        self.result_label = tk.Label(root, text="Результат:", bg='#fff8e7', 
                                     font=("Arial", 12, "bold"))
        self.result_label.pack()
        
        self.result_text = tk.Label(root, text="", bg='#fff8e7', font=("Arial", 12), 
                                   wraplength=500)
        self.result_text.pack(pady=10)
        
    def process(self):
        try:
            # Парсим ввод
            input_str = self.entry.get()
            arr = [int(x.strip()) for x in input_str.split(',')]
            
            # Выбираем алгоритм
            algo_map = {
                "Симметричный": symmetrical_couscous,
                "Хаотичный": chaotic_couscous,
                "Золотой": golden_couscous,
                "Фрактальный": fractal_couscous,
                "Спиральный": spiral_couscous
            }
            
            algorithm = algo_map[self.algo_var.get()]
            result = algorithm(arr)
            
            self.result_text.config(text=f"{result}", fg='#2e8b57')
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Некорректный ввод!\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CouscousApp(root)
    root.mainloop()

# Скачайте репозиторий к себе
git clone https://github.com/sh1sh-sh1sh/symmetrical-couscous.git
cd symmetrical-couscous

# Запустите GUI
python gui/couscous_gui.py
