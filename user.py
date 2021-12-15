from db.core.session import SessionLocal
from db.crud import crud_user
from db.model.user import DB


def session_wrapper(func):
    def wrapper(*args, **kwargs):
        with SessionLocal() as db:
            func(db=db)

    return wrapper


@session_wrapper
def get_user(*args, **kwargs):
    db = kwargs['db']
    res = crud_user.get_by_email(db=db, email="admin@admin.com")
    if res is not None:
        print(res.asjson(DB, ignore_fields=['id']))

get_user()
