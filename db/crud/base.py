from typing import Generic, Optional, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..core.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: str) -> Optional[ModelType]:
        return db.get(self.model, id)

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, id: str, obj_in: UpdateSchemaType) -> int:
        obj_in_data = jsonable_encoder(obj_in)
        result = db.query(self.model).filter(self.model.id == id).update(obj_in_data, synchronize_session='evaluate')
        db.commit()
        return result

    def delete(self, db: Session, *, id: str) -> int:
        result = db.query(self.model).filter(self.model.id == id).delete(synchronize_session='evaluate')
        return result