from sqlalchemy import func, desc, and_

from db import SessionLocal
from models import Student, Group, Teacher, Subject, Grade


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.id,
                Student.full_name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(5)
            .all()
        )
        return result
    finally:
        session.close()


def select_2(subject_id: int):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.id,
                Student.full_name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Grade, Grade.student_id == Student.id)
            .filter(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .first()
        )
        return result
    finally:
        session.close()


def select_3(subject_id: int):
    """
    Знайти середній бал у групах з певного предмета.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Group.id,
                Group.name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .filter(Grade.subject_id == subject_id)
            .group_by(Group.id)
            .order_by(Group.name)
            .all()
        )
        return result
    finally:
        session.close()


def select_4():
    """
    Знайти середній бал на потоці.
    """
    session = SessionLocal()
    try:
        result = session.query(func.round(func.avg(Grade.grade), 2)).scalar()
        return result
    finally:
        session.close()


def select_5(teacher_id: int):
    """
    Знайти які курси читає певний викладач.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.id, Subject.name)
            .filter(Subject.teacher_id == teacher_id)
            .order_by(Subject.name)
            .all()
        )
        return result
    finally:
        session.close()


def select_6(group_id: int):
    """
    Знайти список студентів у певній групі.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Student.id, Student.full_name)
            .filter(Student.group_id == group_id)
            .order_by(Student.full_name)
            .all()
        )
        return result
    finally:
        session.close()


def select_7(group_id: int, subject_id: int):
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.full_name,
                Subject.name,
                Grade.grade,
                Grade.grade_date,
            )
            .join(Grade, Grade.student_id == Student.id)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(
                Student.group_id == group_id,
                Grade.subject_id == subject_id,
            )
            .order_by(Student.full_name, Grade.grade_date)
            .all()
        )
        return result
    finally:
        session.close()


def select_8(teacher_id: int):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(
                Teacher.full_name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade"),
            )
            .join(Subject, Subject.teacher_id == Teacher.id)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(Teacher.id == teacher_id)
            .group_by(Teacher.full_name)
            .first()
        )
        return result
    finally:
        session.close()


def select_9(student_id: int):
    """
    Знайти список курсів, які відвідує певний студент.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.id, Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(Grade.student_id == student_id)
            .distinct()
            .order_by(Subject.name)
            .all()
        )
        return result
    finally:
        session.close()


def select_10(student_id: int, teacher_id: int):
    """
    Список курсів, які певному студенту читає певний викладач.
    """
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.id, Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(
                Grade.student_id == student_id,
                Subject.teacher_id == teacher_id,
            )
            .distinct()
            .order_by(Subject.name)
            .all()
        )
        return result
    finally:
        session.close()