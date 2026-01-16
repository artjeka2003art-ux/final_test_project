from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI(title="GhostCMD Demo App")

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Настройка Jinja2 шаблонов
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Главная страница дашборда"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/status", response_class=HTMLResponse)
async def read_status(request: Request):
    """Страница детального статуса"""
    projects = [
        {
            "id": 1,
            "name": "Ghost Demo API",
            "status": "running",
            "url": "https://example.com/demo",
        },
        {
            "id": 2,
            "name": "Analytics Service",
            "status": "degraded",
            "url": "https://example.com/analytics",
        },
        {
            "id": 3,
            "name": "Database Service",
            "status": "running",
            "url": "https://example.com/db",
        },
    ]
    return templates.TemplateResponse(
        "status.html", {"request": request, "projects": projects}
    )


@app.get("/api/health")
async def health_check():
    """API endpoint для проверки здоровья приложения"""
    return {"status": "ok"}


@app.get("/api/projects")
async def get_projects():
    """API endpoint для получения списка проектов"""
    return [
        {
            "id": 1,
            "name": "Ghost Demo API",
            "status": "running",
            "url": "https://example.com/demo",
        },
        {
            "id": 2,
            "name": "Analytics Service",
            "status": "degraded",
            "url": "https://example.com/analytics",
        },
    ]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
