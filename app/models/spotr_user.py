from typing import Optional
from sqlmodel import Field

from app.schemas.spotr_user import SpotrUserBase


class SpotrUser(SpotrUserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)