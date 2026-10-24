# Web HTTP Lab

A simple FastAPI project created as part of
the Innowise Python Trainee Program.

## Features

- GET /health - checks application health
- GET /hello - returns a greeting message
- Automatic API documentation with Swagger UI
- Automated endpoint tests using TestClient
- GET /notes - returns all notes
- POST /notes - creates a new note (201 Created)
- Pydantic validation for title and content
- In-memory storage with auto-incrementing IDs

## Installation

1. Create a virtual environment.
2. Activate the environment.
3. Install dependencies:
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install -r requirements.txt
   pip install -r requirements.txt

## Run

    uvicorn main:app --reload
    python3 -m uvicorn main:app --reload

Open http://127.0.0.1:8000/docs

## Tests

    python -m pytest -v

## API Endpoints

Method Path Description
GET /health Health check
GET /hello Greeting message
GET /notes List all notes
POST /notes Create a note (201)
GET /notes/{note_id} Get a note by ID (404 if missing)

## API documentation

http://127.0.0.1:8000/docs

## REquest/Responce example

POST/notes
Request
{
"title": "Shopping",
"content": "Buy milk"
}

Responce - HTTP 201
{
"id": 1,
"title": "Shopping",
"content": "Buy milk"
}

## Limitations

Добавь предложение:

Notes are stored in memory, so all data is lost when the application restarts.

Сохрани README через ⌘ + S.

## PostgreSQL Setup

This project uses PostgreSQL to store notes permanently.

### 1. Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Start PostgreSQL

```bash
brew services start postgresql@17
```

### 3. Create database and tables

```bash
/opt/homebrew/opt/postgresql@17/bin/createdb notes_db
/opt/homebrew/opt/postgresql@17/bin/psql -d notes_db -f schema.sql
```

### 4. Configure environment

Create a `.env` file:

```env
DATABASE_URL=postgresql:///notes_db
```

### 5. Run API

```bash
python3 -m uvicorn main:app --reload
```

API documentation: http://127.0.0.1:8000/docs

### Endpoints using PostgreSQL

- GET /notes
- POST /notes
- GET /notes/{note_id}

Notes are stored in PostgreSQL and remain available after restarting the application.
