import os
import sys

from db.core.session import SessionLocal
from db.crud import crud_user
from db.model.user import Create

def init_db() -> None:
    with SessionLocal() as db:
        user = crud_user.get_by_email(db=db, email="admin@admin.com")
        if not user:
            user_obj = Create(
                fullname="admin",
                username="admin",
                email="admin@admin.com",
                password="password",
            )
            crud_user.create(db=db, obj_in=user_obj)


init_db()
