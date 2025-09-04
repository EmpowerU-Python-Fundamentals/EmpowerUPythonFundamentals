URL Redirect & Logging Service

Цей проєкт реалізує сервіс для створення коротких посилань із редіректом та логуванням переходів (IP, User-Agent, час). Передбачена адміністративна панель із базовою авторизацією.

Можливості

-Створення коротких slug to URL у базі даних.
-Редірект користувачів за slug.
-Логування IP-адрес, User-Agent та часу переходу.
-Адмін-панель для додавання та перегляду записів.

Структура проєкту

 iplog/
├── main.py      # Основний застосунок (обробка редіректів)
├── logger.py        # Логування та редірект користувачів
├── admin.py         # Адмін-панель із авторизацією
└── pycache/     # Службові файли Python

Файли

main.py – запускає Flask-сервер, ініціалізує базу urls.db та таблицю urls_mapping. Обробляє запити на редірект.
logger.py – функція log_and_redirect(slug, request), яка перевіряє slug у базі даних, зберігає IP та User-Agent, а також виконує редірект.
admin.py – окремий Flask-додаток для адміністратора. Реалізує авторизацію (логін/пароль беруться зі змінних середовища), додає нові посилання та показує логи.


Встановлення

1. Клонувати репозиторій:

git clone <repo_url>
cd iplog

2. Створити та активувати віртуальне середовище:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Встановити залежності:

pip install flask



Використання

Запуск основного сервера (редіректи)
python -m iplog

Запуск адмін-панелі
python iplog/admin.py

Параметри доступу:
APP_LOGIN – логін адміністратора (за замовчуванням admin)
APP_PASSWORD – пароль адміністратора (за замовчуванням admin)

Можна задати їх через змінні середовища:
export APP_LOGIN=mylogin
export APP_PASSWORD=mypass

База даних

Використовується SQLite (urls.db). Таблиці:
urls_mapping – зберігає slug і цільові URL.
ip_logs – логи (IP, User-Agent, час).


Приклад

1. Додати slug через адмін-панель: myapp → https://example.com
2. Перейти за http://127.0.0.1:5000/myapp
3. Користувача перенаправляє на https://example.com, а IP і User-Agent логуються у базі даних.

Приклади API-запитів

Додавання нового посилання

curl -X POST http://127.0.0.1:5001/create \
     -u admin:admin \
     -H "Content-Type: application/json" \
     -d '{"slug": "myapp", "target_url": "https://example.com"}'

Отримання списку усіх посилань

curl -X GET http://127.0.0.1:5001/urls -u admin:admin

Отримання логів переходів

curl -X GET http://127.0.0.1:5001/logs -u admin:admin

Перевірка редіректу

curl -i http://127.0.0.1:5000/myapp
