from typing import Optional

from sqlalchemy.orm import Session

from .base import CRUDBase
from ..model.user import Create, CreatePasswordHash, Update
from ..schema.user import User


class CRUDUser(CRUDBase[User, CreatePasswordHash, Update]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.email == email).one_or_none()

    def create(self, db: Session, *, obj_in: Create) -> User:
        obj = CreatePasswordHash(fullname=obj_in.fullname, email=obj_in.email, username=obj_in.username, hashed_password=obj_in.password)
        return super().create(db=db, obj_in=obj)


crud_user = CRUDUser(User)
