# GoIT Python Web HW-06

PostgreSQL + SQLAlchemy project for managing students, groups, teachers, subjects, and grades.

## Implemented

- `students` table
- `groups` table
- `teachers` table
- `subjects` table with assigned teacher
- `grades` table with student, subject, grade, and date

## Technologies

- Python
- PostgreSQL
- SQLAlchemy
- Faker
- Docker
- Alembic

## Files

- `db.py` — database connection
- `models.py` — SQLAlchemy ORM models
- `seed.py` — database seeding with random data
- `my_select.py` — 10 required select queries
- `main.py` — helper script to run select queries
- `.env` — database configuration

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
