from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from sqlalchemy.dialects.postgresql import UUID

from app.database.session import engine
from app.models.spotr_user import SpotrUser
from app.schemas.spotr_user import SpotrUserCreate, SpotrUserUpdate, SpotrUserRead

router = APIRouter(prefix="/spotr_user", tags=["spotr_user"])

@router.post("/spotr_user", response_model=SpotrUserRead)
def create_spotr_user(user: SpotrUserCreate):
    with Session(engine) as session:
        spotr_user = SpotrUser.model_validate(user)
        session.add(spotr_user)
        session.commit()
        session.refresh(spotr_user)
        return spotr_user

@router.get("/{id}", response_model=SpotrUserRead)
def get_spotr_user(id: int):
    with Session(engine) as session:
        spotr_user = session.get_one(SpotrUser.id, id)
        if not spotr_user:
            raise HTTPException(status_code=404, detail="User not found")
        return spotr_user

@router.patch("/{id}", response_model=SpotrUserRead)
def update_spotr_user(id: int, updated_spotr_user: SpotrUserUpdate):
    with Session(engine) as session:
        existing_spotr_user = session.get_one(SpotrUser.id, id)
        if not existing_spotr_user:
            raise HTTPException(status_code=404, detail="User not found")

        update_data = updated_spotr_user.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(existing_spotr_user, key, value)

        # no need to run session.add(existing_spotr_user) since sqlAlchemy already keeps track of the changed
        # object and knows what fields change in that object based on setattr
        # commit flushes the changes and updates the DB
        session.commit()
        session.refresh(existing_spotr_user)
        return existing_spotr_user
