from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Conexão SQLite
DB_URL = "sqlite:///wealthhive.db"
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
