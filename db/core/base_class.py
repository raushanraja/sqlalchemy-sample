import json
from typing import Any

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    uuid: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __init__(self, **kwargs):
        class_keys = self.__dict__.keys()

        for key, value in kwargs.items():
            if key in class_keys:
                setattr(self, key, value)

    def asdict(self):
        for c in inspect(self).mapper.column_attrs:
            print(c)
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def asjson(self, Model, ignore_fields=None, include_fields=None) -> json:
        db_obj_dict = self.asdict()

        if include_fields is None:
            include_fields = set(db_obj_dict.keys())
        else:
            include_fields = set(include_fields)

        if ignore_fields is None:
            ignore_fields = {}
        else:
            ignore_fields = set(ignore_fields)

        return Model(**db_obj_dict).json(include=include_fields, exclude=ignore_fields)
