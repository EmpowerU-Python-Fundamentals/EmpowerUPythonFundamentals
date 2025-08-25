import sqlite3
import threading

DB_PATH = 'events.db'
DB_BUFFER_SIZE = 50

class DBBuffer:
    """
    Клас DBBuffer реалізує буферизацію записів у базу даних SQLite.
    """
    def __init__(self, db_path, buffer_size=50):
        """
        Ініціалізує буфер бази даних.
        """
        self.db_path = db_path
        self.buffer_size = buffer_size
        self.buffer = []
        self.lock = threading.Lock()
        self._init_db()

    def _init_db(self):
        """
        Ініціалізує базу даних, створюючи таблицю 'events', якщо вона не існує.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                event_type TEXT,
                path TEXT,
                dest_path TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def add_event(self, timestamp, event_type, path, dest_path=None):
        """
        Додає подію до буфера. Якщо буфер досягає визначеного розміру,
        він автоматично скидається у базу даних.
        """
        with self.lock:
            self.buffer.append((timestamp, event_type, path, dest_path))
            if len(self.buffer) >= self.buffer_size:
                self.flush()

    def flush(self):
        """
        Скидає всі накопичені події з буфера у базу даних.
        """
        if not self.buffer:
            return
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.executemany(
            'INSERT INTO events (timestamp, event_type, path, dest_path) VALUES (?, ?, ?, ?)',
            self.buffer
        )
        conn.commit()
        conn.close()
        self.buffer.clear()

db_buffer = DBBuffer(DB_PATH, DB_BUFFER_SIZE)
