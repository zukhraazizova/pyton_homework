import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:Magazin05@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


Base.metadata.create_all(engine)


@pytest.fixture
def session():
    session = Session()
    yield session
    session.rollback()  # откатываем изменения после каждого теста
    session.close()


def test_add_student(session):
    # Добавление студента
    new_student = Student(name="Иван Иванов")
    session.add(new_student)
    session.commit()

    assert new_student.id is not None

    # Чистим за собой
    session.delete(new_student)
    session.commit()


def test_update_student(session):
    student = Student(name="Пётр Петров")
    session.add(student)
    session.commit()

    # Изменяем имя
    student.name = "Пётр Иванов"
    session.commit()

    updated_student = session.get(Student, student.id)
    assert updated_student.name == "Пётр Иванов"

    # Чистим за собой
    session.delete(updated_student)
    session.commit()


def test_delete_student(session):
    student = Student(name="Сергей Сергеев")
    session.add(student)
    session.commit()

    student_id = student.id

    session.delete(student)
    session.commit()

    deleted_student = session.get(Student, student_id)
    assert deleted_student is None