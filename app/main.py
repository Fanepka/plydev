from dotenv import load_dotenv
from os import getenv

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.services.github import GitHubService

app = FastAPI()

# Подключаем статические файлы (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключаем шаблоны Jinja2
templates = Jinja2Templates(directory="app/templates")

if not load_dotenv('.env'):
    raise ImportError("Not found .env file")

# Инициализация GitHubService
github_service = GitHubService(username="Fanepka", token=getenv("GITHUB_TOKEN"))

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Страница "О себе"
@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    try:
        readme_content = github_service.get_repo_readme("Fanepka")
        return templates.TemplateResponse("about.html", {"request": request, "readme_content": readme_content})
    except Exception as e:
        return templates.TemplateResponse("about.html", {"request": request, "error": str(e)})

# Страница "Проекты"
@app.get("/projects", response_class=HTMLResponse)
async def read_projects(request: Request):
    try:
        repos = github_service.get_user_repos()
        return templates.TemplateResponse("projects.html", {"request": request, "repos": repos})
    except Exception as e:
        return templates.TemplateResponse("projects.html", {"request": request, "error": str(e)})

# Страница "Контакты"
@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.head("/")
async def get_head(request: Request):
    return Response(status_code=200)