from datetime import date

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    students = relationship("Student", back_populates="group")

    def __repr__(self):
        return f"Group(id={self.id}, name='{self.name}')"


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="SET NULL"))

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Student(id={self.id}, full_name='{self.full_name}')"


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)

    subjects = relationship("Subject", back_populates="teacher")

    def __repr__(self):
        return f"Teacher(id={self.id}, full_name='{self.full_name}')"


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="SET NULL"))

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Subject(id={self.id}, name='{self.name}')"


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"), nullable=False)
    grade = Column(Integer, nullable=False)
    grade_date = Column(Date, nullable=False, default=date.today)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

    def __repr__(self):
        return (
            f"Grade(id={self.id}, student_id={self.student_id}, "
            f"subject_id={self.subject_id}, grade={self.grade})"
        )