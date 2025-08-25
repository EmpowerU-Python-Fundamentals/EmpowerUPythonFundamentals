import threading
import time
import logging
import os

from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from db_buffer import db_buffer

class MyHandler(FileSystemEventHandler):
    """
    MyHandler - це користувацький обробник подій файлової системи,
    що успадковується від FileSystemEventHandler Watchdog.
    Він визначає, як реагувати на різні типи подій файлової системи.
    """
    COLOR_MAP = {'created':'green', 'deleted':'red', 'modified':'blue', 'moved':'orange'}

    def __init__(self, callback, events: set):
        """
        Ініціалізує обробник подій.
        """
        super().__init__()
        self.callback = callback
        self.events = events

    def _emit_event(self, event_type: str, path: str, dest_path: str = None):
        """
        Внутрішня допоміжна функція для обробки та відправки подій.
        Записує подію до буфера БД, логує її та оновлює GUI.
        """
        if not path or event_type not in self.events:
            return
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db_buffer.add_event(ts, event_type, path, dest_path)
        msg = f"{event_type.upper()}: {path}" + (f" -> {dest_path}" if dest_path else "")
        logging.info(msg)
        self.callback(ts, event_type, path, dest_path or "")

    def on_created(self, event):
        """
        Обробник події створення файлу/каталогу.
        Викликається Watchdog, коли об'єкт створюється.
        """
        if not event.is_directory:
            self._emit_event('created', event.src_path)

    def on_deleted(self, event):
        """
        Обробник події видалення файлу/каталогу.
        Викликається Watchdog, коли об'єкт видаляється.
        """
        if not event.is_directory:
            self._emit_event('deleted', event.src_path)

    def on_modified(self, event):
        """
        Обробник події модифікації файлу/каталогу.
        Викликається Watchdog, коли об'єкт змінюється.
        """
        if not event.is_directory:
            self._emit_event('modified', event.src_path)

    def on_moved(self, event):
        """
        Обробник події переміщення/перейменування файлу/каталогу.
        Викликається Watchdog, коли об'єкт переміщується або перейменовується.
        """
        if not event.is_directory:
            self._emit_event('moved', event.src_path, event.dest_path)

class WatcherThread(threading.Thread):
    """
    Клас WatcherThread запускає та керує моніторингом файлової системи
    в окремому потоці, щоб не блокувати головний потік GUI.
    """
    def __init__(self, paths, events, callback, status_callback):
        """
        Ініціалізує потік моніторингу.
        """
        super().__init__(daemon=True)
        self.paths = paths
        self.events = events
        self.callback = callback
        self.status_callback = status_callback
        self.observer = Observer()
        self._stopping = threading.Event()

    def run(self):
        """
        Метод, що виконується при запуску потоку.
        Він налаштовує спостерігача Watchdog і запускає моніторинг.
        """
        try:
            handler = MyHandler(self.callback, self.events)
            for p in self.paths:
                if os.path.isdir(p):
                    self.observer.schedule(handler, p, recursive=True)
                else:
                    self.status_callback(f"⚠️ Пропущено неіснуючий шлях: {p}")
            self.observer.start()
            self.status_callback("👀 Моніторинг активний…")
            while not self._stopping.is_set():
                time.sleep(0.2)
        except Exception as e:
            self.status_callback(f"❌ Помилка моніторингу: {e}")
        finally:
            self.observer.stop()
            self.observer.join()
            self.status_callback("⏹ Моніторинг зупинено.")
            db_buffer.flush()

    def stop(self):
        """
        Сигналізує потоку моніторингу про необхідність зупинки.
        """
        self._stopping.set()
