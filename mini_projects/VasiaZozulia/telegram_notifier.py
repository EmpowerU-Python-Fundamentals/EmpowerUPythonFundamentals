import threading
import logging
from urllib import request, parse

class TelegramNotifier:
    """
    Клас для надсилання сповіщень у Telegram.
    """
    def __init__(self, token: str, chat_id: str):
        """
        Ініціалізує об'єкт TelegramNotifier.
        """
        self.token = token.strip()
        self.chat_id = chat_id.strip()

    def enabled(self) -> bool:
        """
        Перевіряє, чи увімкнені сповіщення Telegram (чи встановлені токен і chat ID).
        """
        return bool(self.token and self.chat_id)

    def send_async(self, text: str):
        """
        Надсилає текстове повідомлення у Telegram в окремому потоці.
        Це запобігає зависанню GUI під час очікування відповіді від Telegram API.
        """
        if not self.enabled():
            return
        threading.Thread(target=self._send, args=(text,), daemon=True).start()

    def _send(self, text: str):
        """
        Внутрішня функція для безпосереднього надсилання повідомлення до Telegram API.
        """
        try:
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            data = parse.urlencode({'chat_id': self.chat_id,'text': text}).encode()
            req = request.Request(url, data=data)
            with request.urlopen(req, timeout=10) as resp:
                resp.read()
        except Exception as e:
            logging.error(f"Telegram send failed: {e}")
