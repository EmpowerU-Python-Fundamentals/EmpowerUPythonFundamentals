import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from storage import save_tasks, load_tasks
from models import Task


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=10, fill=tk.X)
        self.task_entry = tk.Entry(self.top_frame, width=40)
        self.task_entry.pack(anchor=tk.CENTER, fill=tk.X)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=5)
        tk.Button(self.buttons_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Set Deadline", command=self.set_deadline_for_selected).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(root, columns=("status", "name", "deadline"), show="headings", height=10)
        self.tree.heading("status", text=" ")
        self.tree.heading("name", text="Task")
        self.tree.heading("deadline", text="Deadline")
        self.tree.column("status", width=30, anchor="center")
        self.tree.column("name", width=250)
        self.tree.column("deadline", width=160, anchor="center")
        self.tree.pack(pady=10, fill=tk.X)

        self.tree.tag_configure('done', background='lightgreen')
        self.tree.tag_configure('in_progress', background='yellow')
        self.tree.tag_configure('failed', background='red')

        #self.tree.bind("<Double-1>", self.on_row_double_click)

        #self.tree.bind("<Delete>", lambda _e: self.delete_task())

        self.status_field = tk.LabelFrame(root, text="Change Status")
        self.status_field.pack(fill=tk.X, padx=5, pady=5)
        self.status_var = tk.StringVar(value="in_progress")
        self.rb_in_progress = tk.Radiobutton(self.status_field, text="In Progress", variable=self.status_var, value="in_progress", command=self.change_status)
        self.rb_done = tk.Radiobutton(self.status_field, text="Done", variable=self.status_var, value="done", command=self.change_status)
        self.rb_failed = tk.Radiobutton(self.status_field, text="Failed", variable=self.status_var, value="failed", command=self.change_status)
        self.rb_in_progress.pack(side=tk.LEFT, padx=5)
        self.rb_done.pack(side=tk.LEFT, padx=5)
        self.rb_failed.pack(side=tk.LEFT, padx=5)

        self.tasks = []
        self.load()

    def add_task(self):
        name = self.task_entry.get().strip()
        if name:
            task = Task(name=name)
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_list()
            self.save()
        else:
            messagebox.showwarning("Warning", "The input field is empty. Please enter a task.")

    def delete_task(self):
        selected = self.tree.selection()
        if selected:
            index = int(selected[0])
            self.tasks.pop(index)
            self.refresh_list()
            self.save()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def on_row_double_click(self, event):
        sel = self.tree.selection()
        idx = int(sel[0])
        task = self.tasks[idx]
        next_status = {
            "in_progress": "done",
            "done": "failed",
            "failed": "in_progress",
        }.get(task.status, "in_progress")
        task.status = next_status
        self.status_var.set(next_status)
        self.refresh_list()
        self.save()

    def save(self):
        save_tasks(self.tasks)


    def load(self):
        self.tasks = load_tasks()
        self.refresh_list()

    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, task in enumerate(self.tasks):
            deadline_text = task.deadline.strftime('%Y-%m-%d %H:%M') if task.deadline else ""
            self.tree.insert("", tk.END, iid=str(i), values=("", task.name, deadline_text), tags=(task.status,))

        def on_select(_event=None):
            sel = self.tree.selection()
            if not sel:
                return
            idx = int(sel[0])
            if 0 <= idx < len(self.tasks):
                self.status_var.set(self.tasks[idx].status)
        self.tree.bind("<<TreeviewSelect>>", on_select)

    def change_status(self):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        if 0 <= idx < len(self.tasks):
            self.tasks[idx].status = self.status_var.get()
            self.refresh_list()
            self.save()

    def set_deadline_for_selected(self):
        try:
            from tkcalendar import Calendar
        except Exception:
            messagebox.showwarning("Warning", "Install tkcalendar: pip install tkcalendar")
            return

        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Warning", "Select a task to set a deadline.")
            return
        idx = int(sel[0])
        if not (0 <= idx < len(self.tasks)):
            return

        win = tk.Toplevel(self.root)
        win.title("Set Deadline")
        win.grab_set()

        cal = Calendar(win, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(padx=10, pady=10)

        time_frame = tk.Frame(win)
        time_frame.pack(pady=5)
        tk.Label(time_frame, text="Hour (0-23)").pack(side=tk.LEFT)
        hour_entry = tk.Entry(time_frame, width=4)
        hour_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(time_frame, text="Minute (0-59)").pack(side=tk.LEFT)
        minute_entry = tk.Entry(time_frame, width=4)
        minute_entry.pack(side=tk.LEFT, padx=5)

        current = self.tasks[idx].deadline
        if current:
            cal.selection_set(current.date())
            hour_entry.insert(0, str(current.hour))
            minute_entry.insert(0, str(current.minute))

        def save_deadline():
            date_text = cal.get_date()
            try:
                hour = int(hour_entry.get() or 0)
                minute = int(minute_entry.get() or 0)
                dt = datetime.strptime(date_text, "%Y-%m-%d").replace(hour=hour, minute=minute)
                self.tasks[idx].deadline = dt
                self.refresh_list()
                self.save()
                win.destroy()
            except Exception:
                messagebox.showwarning("Warning", "Invalid time")

        btns = tk.Frame(win)
        btns.pack(pady=10)
        tk.Button(btns, text="Save", command=save_deadline).pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="Clear", command=lambda: (setattr(self.tasks[idx], 'deadline', None), self.refresh_list(), self.save(), win.destroy())).pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="Cancel", command=win.destroy).pack(side=tk.LEFT, padx=5)
