from fastapi import FastAPI
import uvicorn

from os import environ as env
from os import system

from routers.user_api.main_api import router as main_api
from routers.post_api.post_api import router as post_api

app = FastAPI()
app.include_router(main_api)
app.include_router(post_api)

PORT = int(env.get("PORT"))

system("alembic revision --autogenerate -m \"Init tables\"")
system("alembic upgrade head")
uvicorn.run(app, host="0.0.0.0", port=PORT)
