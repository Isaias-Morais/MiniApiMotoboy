from sqlalchemy.orm import sessionmaker
from database.engine import engine
import os

SessionLocal = sessionmaker(bind=engine)



print("ARQUIVO:", __file__)
print("SessionLocal:", SessionLocal)
print(SessionLocal)