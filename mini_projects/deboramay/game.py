import tkinter as tk
import random
from tkinter import messagebox, ttk

class HangmanGame:
    def __init__(self, root):
        """
        Initializes the main game window and all necessary components.
        """
        self.root = root
        self.root.title("Гра 'Шибениця'")
        
        self.letter_buttons = {}
        self.categories = {
            "IT-терміни": "it_words.txt",
            "Міста світу": "cities_words.txt",
            "Тварини": "animals_words.txt"
        }
        self.create_widgets()
        self.show_category_selection()
    
    def load_words(self, filename):
        """
        Loads a list of words from a specified text file.
        """
        try:
            with open(filename, "r", encoding="utf-8") as file:
                words = [word.strip().upper() for word in file if word.strip()]
        except FileNotFoundError:
            messagebox.showerror("Помилка", f"Файл '{filename}' не знайдено. Будь ласка, перевірте наявність файлів категорій.")
            self.root.destroy()
            raise SystemExit()
        if not words:
            messagebox.showerror("Помилка", f"Файл '{filename}' порожній. Будь ласка, додайте слова до файлу.")
            self.root.destroy()
            raise SystemExit()
        
        return words

    def create_widgets(self):
        """
        Creates and arranges all widgets in the main game window.
        """
        welcome_text = "Вітаю у грі 'Шибениця'.\nСпробуй вгадати слово, в тебе є 6 спроб. Щасти!"
        self.welcome_label = tk.Label(self.root, text=welcome_text, font=("Helvetica", 14), justify="center")
        self.welcome_label.pack(pady=10)
        
        self.game_widgets_frame = tk.Frame(self.root)
        self.game_widgets_frame.pack(pady=20)
        
        self.word_label = tk.Label(self.game_widgets_frame, text="", font=("Helvetica", 32))
        self.word_label.pack()

        self.canvas = tk.Canvas(self.game_widgets_frame, width=200, height=250, bg="white")
        self.canvas.pack(pady=10)
        
        self.attempts_label = tk.Label(self.game_widgets_frame, text="", font=("Helvetica", 14))
        self.attempts_label.pack()

        self.guessed_letters_label = tk.Label(self.game_widgets_frame, text="", font=("Helvetica", 14))
        self.guessed_letters_label.pack()

        letters_frame = tk.Frame(self.game_widgets_frame)
        letters_frame.pack(pady=10)
        ukrainian_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
        row1_frame = tk.Frame(letters_frame)
        row1_frame.pack()
        for letter in ukrainian_alphabet[0:11]:
            btn = tk.Button(row1_frame, text=letter, width=2, height=1, font=("Helvetica", 14),
                            command=lambda l=letter: self.check_guess(l))
            btn.pack(side=tk.LEFT, padx=1, pady=1)
            self.letter_buttons[letter] = btn
        row2_frame = tk.Frame(letters_frame)
        row2_frame.pack()
        for letter in ukrainian_alphabet[11:22]:
            btn = tk.Button(row2_frame, text=letter, width=2, height=1, font=("Helvetica", 14),
                            command=lambda l=letter: self.check_guess(l))
            btn.pack(side=tk.LEFT, padx=1, pady=1)
            self.letter_buttons[letter] = btn
        row3_frame = tk.Frame(letters_frame)
        row3_frame.pack()
        for letter in ukrainian_alphabet[22:]:
            btn = tk.Button(row3_frame, text=letter, width=2, height=1, font=("Helvetica", 14),
                            command=lambda l=letter: self.check_guess(l))
            btn.pack(side=tk.LEFT, padx=1, pady=1)
            self.letter_buttons[letter] = btn

        self.new_game_button = tk.Button(self.game_widgets_frame, text="Нова гра", command=self.show_category_selection)
        self.new_game_button.pack(pady=10)

    def show_category_selection(self):
        """
        Hides the game interface and displays the category selection buttons.
        """
        self.game_widgets_frame.pack_forget()

        self.category_frame = tk.Frame(self.root)
        self.category_frame.pack(pady=50)

        tk.Label(self.category_frame, text="Обери категорію для гри:", font=("Helvetica", 16)).pack(pady=10)

        for name, filename in self.categories.items():
            btn = tk.Button(self.category_frame, text=name, font=("Helvetica", 14), width=20,
                            command=lambda f=filename: self.start_new_game(f))
            btn.pack(pady=5)
    
    def start_new_game(self, category_file):
        """
        Destroys the category selection frame and starts a new game.
        """
        self.category_frame.destroy()
        self.game_widgets_frame.pack()
        self.new_game(category_file)

    def draw_gallows(self):
        """
        Clears the canvas and draws the static gallows structure.
        """
        self.canvas.delete("all")
        self.canvas.create_rectangle(20, 220, 180, 225, fill="black", outline="black")
        self.canvas.create_rectangle(45, 30, 50, 220, fill="black", outline="black")
        self.canvas.create_rectangle(45, 30, 150, 35, fill="black", outline="black")
        self.canvas.create_rectangle(145, 30, 150, 60, fill="black", outline="black")

    def draw_hangman_part(self):
        """
        Draws one part of the hangman figure based on the number of remaining attempts.
        """
        parts = [
            lambda: self.canvas.create_oval(135, 65, 165, 95, width=2, outline="black"),
            lambda: self.canvas.create_line(150, 95, 150, 150, width=2, fill="black"),
            lambda: self.canvas.create_line(150, 110, 120, 130, width=2, fill="black"),
            lambda: self.canvas.create_line(150, 110, 180, 130, width=2, fill="black"),
            lambda: self.canvas.create_line(150, 150, 120, 180, width=2, fill="black"),
            lambda: self.canvas.create_line(150, 150, 180, 180, width=2, fill="black")
        ]
        part_index = 5 - self.attempts
        if 0 <= part_index < len(parts):
            parts[part_index]()
            self.canvas.update_idletasks()

    def update_display(self):
        """
        Updates the displayed word, attempts count, and guessed letters.
        """
        displayed_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        self.word_label.config(text=displayed_word.strip())
        self.attempts_label.config(text=f"Спроб залишилось: {self.attempts}")
        self.guessed_letters_label.config(text=f"Використані літери: {' '.join(sorted(self.guessed_letters))}")

    def check_guess(self, letter):
        """
        Handles a letter guess from the player.
        """
        self.letter_buttons[letter].config(state="disabled")
        if letter in self.guessed_letters:
            return 
        self.guessed_letters.append(letter)
        if letter in self.secret_word:
            self.update_display()
            self.check_win()
        else:
            self.attempts -= 1
            self.draw_hangman_part()
            self.update_display()
            self.check_loss()

    def check_win(self):
        """
        Checks if the player has won the game.
        """
        if all(letter in self.guessed_letters for letter in self.secret_word):
            self.end_game("Вітаємо! Ви відгадали слово!")

    def check_loss(self):
        """
        Checks if the player has lost the game.
        """
        if self.attempts <= 0:
            self.end_game(f"На жаль, ви програли. Слово було: {self.secret_word}")

    def end_game(self, message):
        """
        Ends the current game and displays a message to the player.
        """
        for btn in self.letter_buttons.values():
            btn.config(state="disabled")
        messagebox.showinfo("Гра завершена", message)
        self.show_category_selection()

    def new_game(self, category_file):
        """
        Initializes a new game with a word from the specified category.
        """
        words = self.load_words(category_file)
        
        self.secret_word = random.choice(words).upper()
        self.guessed_letters = []
        self.attempts = 6
        self.canvas.delete("all")
        self.draw_gallows()
        for btn in self.letter_buttons.values():
            btn.config(state="normal")
        self.update_display()