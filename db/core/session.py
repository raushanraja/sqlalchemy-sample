from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URI = "postgresql://post@user.com:postuserpassword@localhost:5432/testdb"


engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, pool_size=10)
session_factory = sessionmaker(autocommit=False, autoflush=True, bind=engine)
SessionLocal = scoped_session(session_factory)
