# GhostCMD Demo App

Небольшое демо-приложение на FastAPI для демонстрации деплоя через GhostCMD.

## Описание

Веб-приложение-дашборд с тёмной темой и изумрудными акцентами, показывающее статус проектов и кластера. Проект создан для демонстрации возможностей AI-powered deployments.

## Структура проекта

```
.
├── main.py                 # Основное FastAPI приложение
├── requirements.txt        # Зависимости проекта
├── README.md              # Документация
└── app/
    ├── __init__.py
    ├── templates/         # HTML шаблоны
    │   ├── base.html
    │   ├── index.html
    │   └── status.html
    └── static/
        └── css/
            └── styles.css
```

## Установка и запуск

1. Создайте виртуальное окружение:
```bash
python -m venv .venv
```

2. Активируйте виртуальное окружение:
```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Запустите приложение:
```bash
python main.py
```

Приложение будет доступно по адресу: http://localhost:8000

## Маршруты

- `GET /` - Главная страница дашборда
- `GET /status` - Страница детального статуса проектов
- `GET /api/health` - API endpoint для проверки здоровья (возвращает `{"status": "ok"}`)
- `GET /api/projects` - API endpoint для получения списка проектов (JSON)

## Технологии

- Python 3.10+
- FastAPI
- Uvicorn
- Jinja2

## Деплой

Проект готов к деплою через GhostCMD или любой другой сервис, поддерживающий Python-приложения.
