from db import SessionLocal
from models import Teacher, Subject, Grade
from my_select import (
    select_1,
    select_2,
    select_3,
    select_4,
    select_5,
    select_6,
    select_7,
    select_8,
    select_9,
    select_10,
)


def print_result(title, result):
    print(f"\n{title}")
    print("-" * len(title))
    if result is None:
        print("No data")
    elif isinstance(result, list):
        if not result:
            print("No data")
        else:
            for row in result:
                print(row)
    else:
        print(result)


def get_valid_teacher_id():
    session = SessionLocal()
    try:
        teacher = (
            session.query(Teacher)
            .join(Subject, Subject.teacher_id == Teacher.id)
            .first()
        )
        return teacher.id if teacher else 1
    finally:
        session.close()


def get_valid_student_teacher_pair():
    session = SessionLocal()
    try:
        row = (
            session.query(Grade.student_id, Subject.teacher_id)
            .join(Subject, Subject.id == Grade.subject_id)
            .first()
        )
        if row:
            return row.student_id, row.teacher_id
        return 1, 1
    finally:
        session.close()


if __name__ == "__main__":
    teacher_id = get_valid_teacher_id()
    student_id, teacher_for_student_id = get_valid_student_teacher_pair()

    print_result("SELECT 1", select_1())
    print_result("SELECT 2 (subject_id=1)", select_2(1))
    print_result("SELECT 3 (subject_id=1)", select_3(1))
    print_result("SELECT 4", select_4())
    print_result(f"SELECT 5 (teacher_id={teacher_id})", select_5(teacher_id))
    print_result("SELECT 6 (group_id=1)", select_6(1))
    print_result("SELECT 7 (group_id=1, subject_id=1)", select_7(1, 1))
    print_result(f"SELECT 8 (teacher_id={teacher_id})", select_8(teacher_id))
    print_result(f"SELECT 9 (student_id={student_id})", select_9(student_id))
    print_result(
        f"SELECT 10 (student_id={student_id}, teacher_id={teacher_for_student_id})",
        select_10(student_id, teacher_for_student_id),
    )