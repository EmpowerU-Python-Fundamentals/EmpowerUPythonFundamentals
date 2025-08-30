import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Функції оцінювання
def score_water_quality(ph, hardness):
    if 6.5 <= ph <= 7.5 and hardness <= 150:
        return 10
    elif 6.0 <= ph <= 8.0:
        return 7
    else:
        return 4

def score_density(start_density, final_density):
    attenuation = (start_density - final_density) / start_density if start_density != 0 else 0
    if 0.7 <= attenuation <= 0.85:
        return 10
    elif 0.6 <= attenuation <= 0.9:
        return 7
    else:
        return 4

def overall_quality(water, density):
    total = water + density
    avg = total / 2
    return round(avg, 2)

# Збереження у Excel 
def save_to_excel(entry):
    excel_file = "beer_quality.xlsx"

    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)
        df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    else:
        df = pd.DataFrame([entry])

# Дані для оцінки
    columns_order = [
        "Назва пива",
        "Дата варки",
        "Оцінка води",
        "Оцінка густини",
        "Клієнт",
        "Оцінка клієнта",
        "Фінальна оцінка"
    ]
    df = df[columns_order]
    df.to_excel(excel_file, index=False)