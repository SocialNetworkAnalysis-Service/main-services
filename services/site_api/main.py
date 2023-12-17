import asyncio

import nats
import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from pathlib import Path
from starlette.middleware.sessions import SessionMiddleware

from src.config_reader import config
from src.dependencies import get_current_username
# from src.dependencies import GetNatsJetStream, nats_jetstream_stub
from src.essence.users.router import router as router_users

app = FastAPI(
    title="SocialNetworkAnalysis-Site",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
app.add_middleware(SessionMiddleware, secret_key="123qwerty")

@app.get("/docs", include_in_schema=False)
async def get_swagger_documentation(username: str = Depends(get_current_username)):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/redoc", include_in_schema=False)
async def get_redoc_documentation(username: str = Depends(get_current_username)):
    return get_redoc_html(openapi_url="/openapi.json", title="docs")


@app.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(get_current_username)):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)


app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "site/src/static"),
    name="static",
)

templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})

@app.get("/chat_bot", response_class=HTMLResponse)
async def chat_bot(request: Request):
    return templates.TemplateResponse("chat_bot.html", {"request": request})


async def main():
    app.include_router(router_users)

    # nc = await nats.connect(config.NATS_SERVER_URL)
    # js = nc.jetstream()

    # try:
    #     await js.create_object_store(config.TEMP_FILES_BUCKET)
    # except TimeoutError:
    #     print("Probably invalid nats server")

    # app.dependency_overrides[nats_jetstream_stub] = GetNatsJetStream(js)

    uvicorn_config = uvicorn.Config(app, host="0.0.0.0", port=8001, log_level="info")
    server = uvicorn.Server(uvicorn_config)

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
