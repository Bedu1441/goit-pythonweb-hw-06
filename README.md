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

Run PostgreSQL in Docker:

docker run --name hw06-postgres -p 5433:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
Environment variables

Example .env:

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5433
Seed database
python seed.py
Run select queries
python main.py

Notes
The project uses SQLAlchemy ORM models and session-based queries.
Random data is generated with Faker.
The database is filled with groups, teachers, subjects, students, and grades.
Alembic dependency is included and project is prepared for migrations.

Additional CLI CRUD functionality was not implemented because it is optional in the assignment and catastrophic lack of time.

## Migrations

Database schema is managed with Alembic migrations.

Initialize database schema:

```bash
alembic upgrade head

Seed data:

python seed.py
```
