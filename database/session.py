from sqlalchemy.orm import create_session
from database.engine import engine

SessionLocal = create_session(bind=engine)