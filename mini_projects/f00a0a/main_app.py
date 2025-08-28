import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

class ReactionTime:
    def __init__(self, root):
        self.root = root
        self.root.title("Test your reaction")
        self.root.geometry("512x512")

        # Game state variables
        self.running = False
        self.start_time = 0.0
        self.attempts_left = 3
        self.total_attempts = 3
        self.attempt_number = 1
        self.target_time = 3 

        self.setup_styles()
        self.create_widgets()
        self.setup_bindings()
        self.reset_game()

    def setup_styles(self):
        """Customizes the appearance (style) of various widgets"""
        style = ttk.Style()
        style.configure("Win.TLabel", foreground="green", font=("Arial", 24, "bold"))
        style.configure("Fail.TLabel", foreground="red", font=("Arial", 24, "bold"))
        style.configure("Neutral.TLabel", foreground="blue", font=("Arial", 24, "bold"))
        style.configure("TButton", font=("Arial", 16), padding=[10, 5])
        style.configure("TLabel", font=("Arial", 16))

    def format_time(self, total_seconds):
        """Converts the total number of seconds into a displayable format"""
        ms = int((total_seconds - int(total_seconds)) * 1000)
        secs = int(total_seconds)
        return f"{secs:02d}.{ms // 10:02d}"

    def update_timer(self):
        """Updates the timer. It recursively calls itself every 10 milliseconds"""
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=self.format_time(elapsed_time))
            self.root.after(10, self.update_timer)

    def start_timer(self):
        """Starts the timer if the game is not yet started and there are attempts left."""
        if not self.running and self.attempts_left > 0:
            self.start_time = time.time()
            self.running = True
            self.update_timer()
            self.message_label.config(text="", style="Neutral.TLabel")

    def stop_timer(self):
        """Stops the timer and checks if the player has won."""
        if not self.running:
            return

        self.running = False
        elapsed_time = time.time() - self.start_time
        is_win = False
        
        # Applying logic according to the current attempt
        if self.attempt_number == 1:
            # Hard
            if int(elapsed_time) == self.target_time and (elapsed_time - self.target_time) < 0.01:
                random_offset = random.randint(1, 14) / 100.0
                adjusted_time = elapsed_time + random_offset
                self.timer_label.config(text=self.format_time(adjusted_time))
                self.message_label.config(text="Almost, try again", style="Fail.TLabel")
            else:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="Almost, try again", style="Fail.TLabel")

        elif self.attempt_number == 2:
            # Normal
            if int(elapsed_time) == self.target_time and (elapsed_time - self.target_time) < 0.01:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="You won!", style="Win.TLabel")
                is_win = True
            else:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="Almost, try again", style="Fail.TLabel")
        
        elif self.attempt_number == 3:
            # Easy
            lower_bound = self.target_time - 0.5
            upper_bound = self.target_time + 0.5
            
            if lower_bound <= elapsed_time <= upper_bound:
                self.timer_label.config(text=self.format_time(float(self.target_time)))
                self.message_label.config(text="You did it!", style="Win.TLabel")
                is_win = True
            else:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="Almost, try again.", style="Fail.TLabel")
        
        if is_win:
            messagebox.showinfo("Congratulations!", "You win a discount! The game is over.")
            self.reset_game()
        else:
            self.attempts_left -= 1
            self.attempt_number += 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
            if self.attempts_left == 0:
                messagebox.showinfo("Game over", f"You have lost. Attempts exhausted.")
                self.reset_game()

    def reset_game(self, event=None):
        """Resets all game variables to their original state."""
        self.running = False
        self.start_time = 0.0
        self.timer_label.config(text="00.00")
        self.message_label.config(text=f"Goal: {self.target_time} c.", style="Neutral.TLabel")
        self.attempts_left = 3
        self.attempt_number = 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

    def start_stop_toggle(self, event=None):
        """This is a toggle function that either starts or stops the timer."""
        if self.running:
            self.stop_timer()
        else:
            self.start_timer()

    def create_widgets(self):
        """Responsible for creating all graphical interface elements"""
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True, fill="both")
        
        self.title_label = ttk.Label(self.main_frame, text="Reaction game, win a discount", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=5)
        
        self.timer_label = ttk.Label(self.main_frame, text="00.00", font=("Arial", 32, "bold"))
        self.timer_label.pack(pady=10)
        
        self.message_label = ttk.Label(self.main_frame, text="", font=("Arial", 24, "bold"))
        self.message_label.pack(pady=(0, 5))
        
        self.attempts_label = ttk.Label(self.main_frame, text=f"Attempts left: {self.attempts_left}", font=("Arial", 18))
        self.attempts_label.pack(pady=5)
        
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady=5)
        
        self.start_button = ttk.Button(self.button_frame, text="Start / Stop (Space)", command=self.start_stop_toggle)
        self.start_button.pack(side="left", padx=5)
        
        self.reset_button = ttk.Button(self.button_frame, text="Reset (Esc)", command=self.reset_game)
        self.reset_button.pack(side="left", padx=5)

    def setup_bindings(self):
        """Binds hotkeys"""
        self.root.bind('<space>', self.start_stop_toggle)
        self.root.bind('<Escape>', self.reset_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = ReactionTime(root)
    root.mainloop()