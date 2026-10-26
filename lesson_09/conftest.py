import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "postgresql+psycopg2://postgres:Nikbali_95@localhost:5432/QA"

engine = create_engine(DB_URL, echo=False, future=True)

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


Base.metadata.create_all(bind=engine)
print("Таблицы students, teachers, subjects созданы (или проверены)")

SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
    )


@pytest.fixture(scope="function")
def db_session():
    """Фикстура для создания сессии с транзакцией."""
    conn = engine.connect()
    tx = conn.begin()
    session = SessionLocal(bind=conn)

    try:
        yield session
    finally:
        session.close()
        tx.rollback()
        conn.close()
