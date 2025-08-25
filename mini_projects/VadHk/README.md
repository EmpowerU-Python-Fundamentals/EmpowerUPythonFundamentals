<!-- @format -->

# API

[Commands]

- Start/shut containers with project: docker-compose up/down
- Start server: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

[DataBase]

- docker exec -it postgres_db psql -U admin -d main_db
- /dt (show all tables)
- SELECT \* FROM users; (example)

[Pages]

- /docs (swagger)

[Description]
Simple API miniproject with using Docker and FastAPI framework, as a DB use PostgreSQL.

[Structure]
project/
├── app/
│ ├── api/ # Роутери (розділені по ресурсах)
│ │ ├── v1/
│ │ │ ├── users.py
│ │ │ ├── tasks.py
│ │ │ └── **init**.py
│ ├── core/ # Налаштування (JWT, CORS, логування)
│ │ ├── config.py
│ │ ├── security.py
│ │ └── **init**.py
│ ├── db/ # Підключення до бази, сесії
│ │ ├── base.py
│ │ ├── session.py
│ │ └── **init**.py
│ ├── models/ # SQLAlchemy-моделі
│ │ ├── user.py
│ │ ├── task.py
│ │ └── **init**.py
│ ├── schemas/ # Pydantic-схеми
│ │ ├── user.py
│ │ ├── task.py
│ │ └── **init**.py
│ ├── services/ # Бізнес-логіка
│ │ ├── user_service.py
│ │ └── task_service.py
│ ├── repositories/ # CRUD-операції
│ │ ├── user_repo.py
│ │ └── task_repo.py
│ ├── main.py # Точка входу
│ └── **init**.py
├── tests/ # Тести
│ ├── conftest.py
│ ├── test_users.py
│ └── test_tasks.py
├── .env
├── docker-compose.yml
├── Dockerfile
└── requirements.txt

[Blueprint]
🔧 1. Тестування та структура
• Створити tests/ з підпапками для unit, integration, e2e
• Налаштувати pytest, coverage, factory_boy для моків
• Додати фікстури для бази даних у тестовому середовищі

🚀 2. Автоматизація та CI/CD
• Налаштувати GitHub Actions або GitLab CI для автоматичного запуску тестів
• Додати лінтери (ruff, black, mypy) до пайплайну
• Створити скрипти для деплойменту (наприклад, через Docker Swarm або на VPS)

🧩 3. Розширення API
• Додати нові ендпоінти з валідацією через Pydantic
• Впровадити авторизацію (JWT або OAuth2)
• Додати throttling, rate limiting, логування запитів

📦 4. Архітектурна еволюція
• Перейти на DDD-підхід: розділити домен, сервіси, репозиторії
• Впровадити dependency injection через fastapi.Depends або wired
• Створити окремі пакети для бізнес-логіки
