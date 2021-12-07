from db.core.session import SessionLocal
from db.crud import crud_user
from db.model.user import DB

with SessionLocal() as db:
    res = crud_user.get_by_email(db=db, email="admin@admin.com")
    print(res.asjson(DB,ignore_fields=['id']))
