#### Alembic Initial Setup
1. initialize the alembic for a project
  + `alembic init alembic`
2. Edit `alembic.ini` file in root directory
  + This is the file that alembic looks for when invoked.
  + Important config for postgres:
    + sqlalchemy.url = postgresql://admin@admin.com:password@localhost:5432/test
3. Create a migration
  + `alembic revision -m "create account table"`
4. Apply migration
  + `alembic upgrade hear`
5. Edit `alembic/env.py` & add Base class for initializing the db