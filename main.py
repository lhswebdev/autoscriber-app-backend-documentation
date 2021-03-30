from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from basemodels import User, TranscriptEntry
import uuid
import tempfile
import os
import random
import string
# Not needed for code, but dependencies needed for requirements
import aiofiles
import uvicorn


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
DOMAIN = "http://localhost:8000"

# Connect to mysql db
conn = sqlite3.connect('autoscriber.db', check_same_thread=False)


# Setting up sql - Creating Tables
def sql_setup():
    unprocessed = '''
        CREATE TABLE IF NOT EXISTS unprocessed (
            meeting_id char(38) NOT NULL,
            uid char(38) NOT NULL,
            name varchar(255) NOT NULL,
            dialogue LONGTEXT NOT NULL,
            time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (meeting_id, time)
        );
    '''
    processed = '''
        CREATE TABLE IF NOT EXISTS processed (
            meeting_id char(38) NOT NULL,
            notes LONGTEXT NOT NULL,
            download_link TINYTEXT NOT NULL,
            date DATETIME NOT NULL DEFAULT CURRENT_DATE,
            PRIMARY KEY (meeting_id)
        );
    '''
    meetings = '''
        CREATE TABLE IF NOT EXISTS meetings (
            meeting_id char(38) NOT NULL,
            host_uid char(38) NOT NULL,
            PRIMARY KEY (meeting_id)
        );
    '''
    for e in (unprocessed, processed, meetings):
        conn.execute(e)
    conn.commit()
    print("Tables are ready!")
sql_setup()

# Returns a meetingID with the length of 10; makes sure that uuid isn't taken
def meetingIDCreator():
    
    


# Client makes get request
# Server responds with User dict (Generate new UUID and meeting id (use meetingID Creator))
@app.post("/host")
def host_meeting():
    user = {'meeting_id': str(meetingIDCreator()), 'uid': str(uuid.uuid4())}
    # Create meeting in meetings db

    return user


# Client makes post request with a dictionary that has "meeting_id" & "name" key
# Server responds with User dict
@app.post("/join")
def join_meeting(user: User):
    user = user.dict()

    # Check with database if meeting exists

    return user

# Client gives server blobs to trasncript
# Add to `unprocessed` table
@app.post("/add")
def add_to_transcript(transcript_entry: TranscriptEntry):
    user = transcript_entry.user

    # Check with `unprocessed` if meeting exists


    # Add blob to uprocessed table

# Client makes request to server to end meeting
# Server removes the meeting from `meetings` table and creates a download link for the fininshed trascript (use md_format())
@app.post("/end")
def end_meeting(user: User):
    user = user.dict()

    # Check `meetings` table to confirm that user is meeting host

    # Get dialogue blobs from `unprocessed` table


    # Now that meeting is ended, we can clean db of all dialogue from the meeting
    # Delete all rows from `unprocessed` & `meetings` where meeting_id = user's meeting_id


    # Format transcript for autoscriber.summarize()
    # Each line looks like this: "Name: dialogue" and all lines are joined with \n
    transcript = "\n".join([": ".join(line) for line in dialogue])

    # Summarize notes using autoscriber.summarize()
    # notes = summarize(transcript) MD CLUB HAS NOT FINISHED THE AI YET
    notes = md_format(transcript)

    # Generate download link
    download_link = f"{DOMAIN}/download?id={user['meeting_id']}"

    # Insert notes into processed table

    return {"notes": notes, "download_link": download_link}

# Helper Function
# formats blobs  with markdown bulletpoints
def md_format(notes):
    
    return md

# Client asks for download after meeting over
# checks for meeting notes and retrievs transcript date from `processed` table 
# writes file called date-note.md
@app.get("/download")
def download_notes(id: str):
    # Query `notes` and `dates` from  `processed` table from notes


    # Create md file for file response
    # note, date are from the sql database
    md_file = tempfile.NamedTemporaryFile(delete=False, suffix='.md')
    fname = f'{date.date()}-notes.md'
    md_file.write(bytes(notes, encoding='utf-8'))
    return FileResponse(md_file.name, media_type="markdown", filename=fname)
