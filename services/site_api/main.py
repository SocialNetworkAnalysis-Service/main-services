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
from fastapi.middleware.cors import CORSMiddleware

from src.config_reader import config
from src.dependencies import get_current_username
# from src.dependencies import GetNatsJetStream, nats_jetstream_stub
from src.essence.users.router import router as router_users
from src.essence.operations.router import router as router_operations

app = FastAPI(
    title="SocialNetworkAnalysis-Site-API",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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



async def main():
    app.include_router(router_users)
    app.include_router(router_operations)

    # nc = await nats.connect(config.NATS_SERVER_URL)
    # js = nc.jetstream()

    # try:
    #     await js.create_object_store(config.TEMP_FILES_BUCKET)
    # except TimeoutError:
    #     print("Probably invalid nats server")

    # app.dependency_overrides[nats_jetstream_stub] = GetNatsJetStream(js)

    uvicorn_config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(uvicorn_config)

    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
