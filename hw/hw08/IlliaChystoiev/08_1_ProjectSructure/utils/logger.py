def log_in_file(message, filename="app.log"):
    """Записує повідомлення у файл журналу."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(str(message) + "\n")

__all__ = ["log_in_file"]