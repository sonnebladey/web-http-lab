from fastapi import FastAPI 
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, HTTPException, Response
from database import get_connection 
from psycopg.rows import dict_row

app = FastAPI(title = "Notes API", version = "0.1.0")

@app.get("/health")
def health():
    return {
        "status":"ok"
    }


@app.head("/health")
def head_health():
    return Response(status_code=200)


@app.get("/hello")
def hello():
    return{
        "message":"Hello from Notes API"
    }

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=80)
    content: str = Field(..., min_length=1, max_length=500)
    user_id: int = Field(..., ge=1) #ge means >= 

notes = []
next_id = 1

@app.get("/notes")
def get_notes(user_id: int | None = None):
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor: #connection to db
            if user_id is not None: 
                cursor.execute(
                    "SELECT id, title, content, user_id FROM notes WHERE user_id = %s", 
                    (user_id,)
                )
            else: 
                cursor.execute(
                    "SELECT id, title, content, user_id FROM notes"
                )
            return cursor.fetchall()
          


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    with get_connection() as conn: #automatic commit rollback 
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(  # %splaceholder for values which are held separately
                """
                INSERT INTO notes (title, content, user_id)
                VALUES (%s, %s, %s) 
                RETURNING id, title, content, user_id
                """,
                (
                    note.title,
                    note.content,
                    note.user_id
                ),  # parameterized query safety from sql injection
            )
            return cursor.fetchone() #receives one line of result 


@app.get("/notes/{note_id}")
def get_note(note_id:int):
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor: # where id looks for concrete id 
            cursor.execute(
                "select id, title, content, user_id FROM notes WHERE id = %s", 
                (note_id,)
            )
            #note_id id as a sql variable, we nedd ',' so pyhton could recognise the set with one value 
            note = cursor.fetchone() # one line or none 
            
            if note is None:
                raise HTTPException(
                    status_code = 404, 
                    detail = "Note not found"
                )
            return note



class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=80)
    content: str | None = Field(default=None, min_length=1, max_length=500)


@app.patch("/notes/{note_id}")
def update_note(note_id: int, update: NoteUpdate):
    for note in notes:
        if note["id"] == note_id:
            if update.title is not None:
                note["title"] = update.title

            if update.content is not None:
                note["content"] = update.content

            return note

    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int):
    for index, note in enumerate(notes):
        if note["id"] == note_id:
            notes.pop(index)
            return Response(status_code=204)

    raise HTTPException(status_code=404, detail="Note not found")
