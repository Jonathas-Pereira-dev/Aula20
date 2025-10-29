from sqlalchemy import create_engine
from sqlalchemy.orm import declaratve_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

engine = create_engine(POSTGRES_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declaratve_base #ORM

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


