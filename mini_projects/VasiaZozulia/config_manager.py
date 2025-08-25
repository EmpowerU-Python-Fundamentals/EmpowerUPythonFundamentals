import os
import yaml
import logging

FOLDERS_FILE = "folders.yaml"
CONFIG_FILE = "config.yaml"

def save_folders(paths):
    """
    Зберігає список шляхів до відстежуваних папок у YAML-файл.
    """
    try:
        with open(FOLDERS_FILE, 'w', encoding='utf-8') as f:
            yaml.safe_dump(paths, f)
    except Exception as e:
        logging.error(f"Save folders failed: {e}")

def load_folders():
    """
    Завантажує список шляхів до відстежуваних папок з YAML-файлу.
    """
    if os.path.exists(FOLDERS_FILE):
        try:
            with open(FOLDERS_FILE, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or []
        except Exception as e:
            logging.error(f"Load folders failed: {e}")
    return []

def save_config(app):
    """
    Зберігає загальну конфігурацію програми (шляхи, фільтри подій, налаштування Telegram)
    у YAML-файл.
    """
    data = {
        'paths': app.paths,
        'events': [ev for ev,var in app.ev_vars.items() if var.get()],
        'telegram': {
            'token': app.tg_token.get(),
            'chat_id': app.tg_chat.get()
        }
    }
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f)
    except Exception as e:
        logging.error(f"Failed to save config: {e}")

def load_config():
    """
    Завантажує конфігурацію програми з YAML-файлу.
    """
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            logging.error(f"Failed to load config: {e}")
    return {}
