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

   pip install -r requirements.txt

## Run

    uvicorn main:app --reload

Open http://127.0.0.1:8000/docs

## Tests

    python -m pytest -v
