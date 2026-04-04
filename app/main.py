from fastapi import FastAPI

from app.database.session import create_db_and_tables
from app.routes.spotr_user import router as user_router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(user_router)