__all__ = ["log_in_file"]


def log_in_file(message: str, filename: str = "log.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(message + "\n")
