# Імпорт функцій безпосередньо з підмодулів.
from .admin import create_admin
from .user import create_user

# Тепер __all__ просто перелічує функції, які мають бути доступні.
__all__ = ["create_admin", "create_user"]