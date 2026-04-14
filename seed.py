import random
from datetime import timedelta

from faker import Faker

from db import SessionLocal, engine, Base
from models import Group, Student, Teacher, Subject, Grade


fake = Faker()


def seed_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    try:
        groups = [
            Group(name="Group A"),
            Group(name="Group B"),
            Group(name="Group C"),
        ]
        session.add_all(groups)
        session.commit()

        teachers = [
            Teacher(full_name=fake.name()) for _ in range(4)
        ]
        session.add_all(teachers)
        session.commit()

        subject_names = [
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology",
            "History",
            "English",
            "Programming",
        ]

        subjects = []
        for name in subject_names:
            teacher = random.choice(teachers)
            subjects.append(Subject(name=name, teacher_id=teacher.id))

        session.add_all(subjects)
        session.commit()

        students = []
        for _ in range(40):
            group = random.choice(groups)
            students.append(Student(full_name=fake.name(), group_id=group.id))

        session.add_all(students)
        session.commit()

        all_students = session.query(Student).all()
        all_subjects = session.query(Subject).all()

        grades = []
        for student in all_students:
            count_grades = random.randint(10, 20)
            for _ in range(count_grades):
                subject = random.choice(all_subjects)
                grade_value = random.randint(60, 100)
                grade_date = fake.date_between(start_date="-1y", end_date="today")
                grades.append(
                    Grade(
                        student_id=student.id,
                        subject_id=subject.id,
                        grade=grade_value,
                        grade_date=grade_date,
                    )
                )

        session.add_all(grades)
        session.commit()

        print("Database seeded successfully.")

    except Exception as error:
        session.rollback()
        print(f"Seed error: {error}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()