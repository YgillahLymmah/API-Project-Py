from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URL = 'sqlite://db.sqlite3'

engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL, connect_args = {
        "check_same_thread": False
    })

sessionLocal = sessionmaker(autocommit=False, 
                            autoflush= False
                            bind=engine)

base = declarative_base()

def get_db():
    db = sessionLocal()
    try: 
        yield db
    except:
        db.close()