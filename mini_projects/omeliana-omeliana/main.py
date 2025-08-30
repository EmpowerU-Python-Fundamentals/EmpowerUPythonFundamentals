***
Програма аналізує якість партії пива на основі:

 Якість води (рН, жорсткість, мінерали)

 Густина/щільність (початкова/кінцева)

 Відгук клієнта (оцінка 1-10)
***
import tkinter as tk
from tkinter import messagebox
from functions import (
    score_water_quality,
    score_density,
    overall_quality,
    save_to_excel
)

# ---- Функція обробки форми ----
def submit():
    try:
        beer_name = entry_beer.get()
        brew_date = entry_date.get()
        client_name = entry_client.get()
        client_score = float(entry_client_score.get() or 0)
        ph = float(entry_ph.get() or 0)
        hardness = float(entry_hardness.get() or 0)
        start_density = float(entry_start_density.get() or 0)
        final_density = float(entry_final_density.get() or 0)

        # Оцінка води та густини
        water = score_water_quality(ph, hardness)
        density = score_density(start_density, final_density)
        final = overall_quality(water, density)

        new_entry = {
            "Назва пива": beer_name,
            "Дата варки": brew_date,
            "Оцінка води": water,
            "Оцінка густини": density,
            "Клієнт": client_name,
            "Оцінка клієнта": client_score,
            "Фінальна оцінка": final
        }

        save_to_excel(new_entry)

        entry_final_score.config(state="normal")
        entry_final_score.delete(0, tk.END)
        entry_final_score.insert(0, str(final))
        entry_final_score.config(state="readonly")

        messagebox.showinfo("Успіх", f"Дані для {beer_name} збережено!\nФінальна оцінка: {final}")

    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числові значення у всі поля.")
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

# ---- Інтерфейс ----
root = tk.Tk()
root.title("Оцінка якості пива")
root.geometry("600x500")

entry_width = 30
pady_val = (12, 0)

tk.Label(root, text="Назва пива").grid(row=0, column=0, sticky="w", pady=pady_val)
entry_beer = tk.Entry(root, width=entry_width)
entry_beer.grid(row=0, column=1, pady=pady_val)

tk.Label(root, text="Дата варки (ДД.ММ.РРРР)").grid(row=1, column=0, sticky="w", pady=pady_val)
entry_date = tk.Entry(root, width=entry_width)
entry_date.grid(row=1, column=1, pady=pady_val)

tk.Label(root, text="pH води").grid(row=2, column=0, sticky="w", pady=pady_val)
entry_ph = tk.Entry(root, width=entry_width)
entry_ph.grid(row=2, column=1, pady=pady_val)

tk.Label(root, text="Жорсткість води").grid(row=3, column=0, sticky="w", pady=pady_val)
entry_hardness = tk.Entry(root, width=entry_width)
entry_hardness.grid(row=3, column=1, pady=pady_val)

tk.Label(root, text="Початкова густина").grid(row=4, column=0, sticky="w", pady=pady_val)
entry_start_density = tk.Entry(root, width=entry_width)
entry_start_density.grid(row=4, column=1, pady=pady_val)

tk.Label(root, text="Кінцева густина").grid(row=5, column=0, sticky="w", pady=pady_val)
entry_final_density = tk.Entry(root, width=entry_width)
entry_final_density.grid(row=5, column=1, pady=pady_val)

tk.Label(root, text="Клієнт").grid(row=6, column=0, sticky="w", pady=pady_val)
entry_client = tk.Entry(root, width=entry_width)
entry_client.grid(row=6, column=1, pady=pady_val)

tk.Label(root, text="Оцінка клієнта (0-10)").grid(row=7, column=0, sticky="w", pady=pady_val)
entry_client_score = tk.Entry(root, width=entry_width)
entry_client_score.grid(row=7, column=1, pady=pady_val)

tk.Label(root, text="Фінальна оцінка").grid(row=8, column=0, sticky="w", pady=pady_val)
entry_final_score = tk.Entry(root, width=entry_width, state="readonly")
entry_final_score.grid(row=8, column=1, pady=pady_val)

tk.Button(root, text="Зберегти", command=submit).grid(row=9, column=0, columnspan=2, pady=20)

root.mainloop()