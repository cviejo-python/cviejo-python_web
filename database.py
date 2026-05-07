import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Crear la base directamente en la raíz del proyecto
db_path = os.path.join(BASE_DIR, "productos.db")

engine = create_engine(
    f"sqlite:///{db_path}",
    echo=False
)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass