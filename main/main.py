from fastapi import FastAPI
import uvicorn

from os import environ as env
from os import system

from router.main_api import router as main_api

app = FastAPI()
app.include_router(main_api)

PORT = int(env.get("PORT"))

system("alembic revision --autogenerate -m \"Init tables\"")
system("alembic upgrade head")
uvicorn.run(app, host="0.0.0.0", port=PORT)
