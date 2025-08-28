import tkinter as tk
from tkinter import ttk, messagebox
import time
import random

class ReactionTime:
    def __init__(self, root):
        self.root = root
        self.root.title("Demo_version")
        self.root.geometry("600x600")

        # Game state variables
        self.running = False
        self.start_time = 0.0
        self.reference_running = False
        self.reference_start_time = 0.0
        self.attempts_left = 0
        self.total_attempts = 0

        self.setup_styles()
        self.create_widgets()
        self.setup_bindings()
        self.reset_game()

    def setup_styles(self):
        style = ttk.Style()
        style.configure("Win.TLabel", foreground="green", font=("Arial", 24, "bold"))
        style.configure("Fail.TLabel", foreground="red", font=("Arial", 24, "bold"))
        style.configure("Neutral.TLabel", foreground="gray", font=("Arial", 24, "bold"))
        style.configure("TCombobox", font=("Arial", 10))
        style.configure("TCombobox.Entry", padding=[5, 5])
        style.configure("TCombobox.Popdown.Label", font=("Arial", 16))
        style.configure("TCombobox.Popdown.TLabel", font=("Arial", 16))
        style.configure("TButton", font=("Arial", 18), padding=[5, 5])
        style.configure("TLabel", font=("Arial", 18))

    def format_time(self, total_seconds):
        ms = int((total_seconds - int(total_seconds)) * 1000)
        secs = int(total_seconds)
        return f"{secs:02d}.{ms // 10:02d}"

    def update_timer(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=self.format_time(elapsed_time))
            self.root.after(10, self.update_timer)

    def start_timer(self):
        if not self.running and self.attempts_left > 0:
            self.start_time = time.time()
            self.running = True
            self.update_timer()

    def stop_timer(self):
        if not self.running:
            return

        self.running = False
        self.reference_running = False
        elapsed_time = time.time() - self.start_time
        
        difficulty = self.difficulty_combo.get()
        selected_time_str = self.time_combo.get()
        
        is_win = False
        
        if difficulty == "Easy":
            target_time = int(selected_time_str)
            lower_bound = target_time - 0.5
            upper_bound = target_time + 0.5
            
            if lower_bound <= elapsed_time <= upper_bound:
                self.timer_label.config(text=self.format_time(float(target_time)))
                self.message_label.config(text="You did it!", style="Win.TLabel")
                is_win = True
            else:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="Almost, try again.", style="Fail.TLabel")
        
        elif difficulty == "Normal":
            target_time = int(selected_time_str)
            if int(elapsed_time) == target_time and (elapsed_time - target_time) < 0.01:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="You won!", style="Win.TLabel")
                is_win = True
            else:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="Almost, try again", style="Fail.TLabel")
                
        elif difficulty == "Hard":
            target_time = int(selected_time_str)
            
            if int(elapsed_time) == target_time and (elapsed_time - target_time) < 0.01:
                random_offset = random.randint(1, 14) / 100.0
                adjusted_time = elapsed_time + random_offset
                self.timer_label.config(text=self.format_time(adjusted_time))
                self.message_label.config(text="Almost, try again", style="Fail.TLabel")
            else:
                self.timer_label.config(text=self.format_time(elapsed_time))
                self.message_label.config(text="Almost, try again", style="Fail.TLabel")
                
        else:
            self.timer_label.config(text=self.format_time(elapsed_time))
            self.message_label.config(text="", style="Neutral.TLabel")

        if not is_win:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
            if self.attempts_left == 0:
                messagebox.showinfo("Game over", f"You have lost. Attempts exhausted.")
                self.reset_game()
        else:
            messagebox.showinfo("Congratulations!", "You win! The game is over.")
            self.reset_game()

    def reset_game(self):
        self.reset_timers_only()
        self.attempts_left = int(self.attempts_combo.get())
        self.total_attempts = self.attempts_left
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")

    def reset_timers_only(self, event=None):
        self.running = False
        self.start_time = 0.0
        self.timer_label.config(text="00.00")
        self.message_label.config(text="", style="Neutral.TLabel")
        self.reference_running = False
        self.reference_start_time = 0.0
        self.reference_timer_label.config(text="00.00")

    def start_stop_toggle(self, event=None):
        if self.running:
            self.stop_timer()
        else:
            self.start_timer()
            self.start_reference_timer()

    def start_reference_timer(self):
        if not self.reference_running:
            self.reference_start_time = time.time()
            self.reference_running = True
            self.update_reference_timer()

    def update_reference_timer(self):
        if self.reference_running:
            elapsed_time = time.time() - self.reference_start_time
            self.reference_timer_label.config(text=self.format_time(elapsed_time))
            self.root.after(10, self.update_reference_timer)

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(expand=True, fill="both")
        
        self.title_label = ttk.Label(self.main_frame, text="Choose game settings", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=5)
        
        self.difficulty_label = ttk.Label(self.main_frame, text="mode:", style="TLabel")
        self.difficulty_label.pack(pady=(5, 5))
        difficulties = ["Easy", "Normal", "Hard"]
        self.difficulty_combo = ttk.Combobox(self.main_frame, values=difficulties, state="readonly", width=16)
        self.difficulty_combo.set(difficulties[0])
        self.difficulty_combo.pack()
        
        self.time_label = ttk.Label(self.main_frame, text="Time (seconds):", style="TLabel")
        self.time_label.pack(pady=(5, 5))
        times = ["3", "5", "10"]
        self.time_combo = ttk.Combobox(self.main_frame, values=times, state="readonly", width=16)
        self.time_combo.set(times[0])
        self.time_combo.pack()
        
        self.attempts_label_text = ttk.Label(self.main_frame, text="Number of attempts:", style="TLabel")
        self.attempts_label_text.pack(pady=(5, 5))
        attempts = ["3", "5", "10"]
        self.attempts_combo = ttk.Combobox(self.main_frame, values=attempts, state="readonly", width=16)
        self.attempts_combo.set(attempts[0])
        self.attempts_combo.pack()
        
        self.timer_label = ttk.Label(self.main_frame, text="00.00", font=("Arial", 24, "bold"))
        self.timer_label.pack(pady=20)
        
        self.message_label = ttk.Label(self.main_frame, text="", font=("Arial", 24, "bold"))
        self.message_label.pack(pady=(5, 5))
        
        self.attempts_label = ttk.Label(self.main_frame, text=f"Attempts left: {self.attempts_combo.get()}", font=("Arial", 16))
        self.attempts_label.pack(pady=5)
        
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(pady=5)
        
        self.start_button = ttk.Button(self.button_frame, text="Start (space)", command=self.start_stop_toggle)
        self.start_button.pack(side="left", padx=5)
        
        self.reset_button = ttk.Button(self.button_frame, text="Reset (esc)", command=self.reset_game)
        self.reset_button.pack(side="left", padx=5)
        
        self.reference_label = ttk.Label(self.main_frame, text="Current time:", font=("Arial", 24, "italic"))
        self.reference_label.pack(pady=(10, 2))
        self.reference_timer_label = ttk.Label(self.main_frame, text="00.00", font=("Arial", 24))
        self.reference_timer_label.pack()

    def setup_bindings(self):
        self.root.bind('<space>', self.start_stop_toggle)
        self.root.bind('<Escape>', self.reset_timers_only)

# Main part of the script
if __name__ == "__main__":
    root = tk.Tk()
    game = ReactionTime(root)
    root.mainloop()