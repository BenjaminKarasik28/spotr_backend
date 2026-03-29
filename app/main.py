from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI(title="Spotr_Api")

class SpotrUser(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None)
    email: str = Field(default=None)
    gym: str = Field(default=None)
    city: str = Field(default=None)

engine = create_engine("sqlite:///spotr.db")
SQLModel.metadata.create_all(engine)
@app.get("/user/{name}")
def fetch_by_name(name: str):
    with Session(engine) as session:
        statement = select(SpotrUser).where(SpotrUser.name == name)
        user = session.exec(statement).first()
        return {"user": user}

@app.post(
    "/create/user")
def create_users(user: SpotrUser):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return {"user": user}