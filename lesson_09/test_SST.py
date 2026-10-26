from conftest import Student, Teacher, Subject


def test_add_student(db_session):
    """Тест на добавление студента."""
    new_student = Student(name="Никита Петрович", age=20)
    db_session.add(new_student)
    db_session.commit()

    result = db_session.query(Student).filter(
        Student.name == "Никита Петрович").first()
    assert result is not None
    assert result.name == "Никита Петрович"
    assert result.age == 20


def test_update_teacher(db_session):
    """Тест на изменение учителя."""
    teacher = Teacher(name="Анна Сидорова")
    db_session.add(teacher)
    db_session.commit()
    original_id = teacher.id

    teacher.name = "Анна Петрова"
    db_session.commit()

    updated = db_session.query(Teacher).filter(
        Teacher.id == original_id).first()
    assert updated is not None
    assert updated.name == "Анна Петрова"


def test_delete_subject(db_session):
    """Тест на удаление предмета."""
    subject = Subject(title="Математика")
    db_session.add(subject)
    db_session.commit()
    subject_id = subject.id

    db_session.delete(subject)
    db_session.commit()

    deleted = db_session.query(Subject).filter(
        Subject.id == subject_id).first()
    assert deleted is None
