from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from basemodels import User, TranscriptEntry
from autoscriber import summarize
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
DOMAIN = ""
# Get environ variables
USER = os.environ.get('SQL_USER')
PASSWORD = os.environ.get('SQL_PASS')
# Connect to mysql db
db = mysql.connector.connect(
    host="localhost",
    user=USER,
    password=PASSWORD,
    database="autoscriber_app"
)
mycursor = db.cursor()


# Setting up sql - Creating Tables
def sql_setup():
    unprocessed = '''
        
    '''
    processed = '''
        
    '''
    meetings = '''
        
    '''
   
    print("Tables are ready!")
sql_setup()


# Returns a meetingID with the length of 10; makes sure that uuid isn't taken
def meetingIDCreator():
    
    


# Client makes get request
# Server responds with User dict (Generate new UUID and meeting id (use meetingID Creator))
@app.post("/host")
def host_meeting():
   
    return user


# Client makes post request with a dictionary that has "meeting_id" & "name" key
# Server responds with User dict
@app.post("/join")
def join_meeting(user: User):
    
    return user

# Client gives server blobs to trasncript
# Add to `unprocessed` table
@app.post("/add")
def add_to_transcript(transcript_entry: TranscriptEntry):


# Client makes request to server to end meeting
# Server removes the meeting from `meetings` table and creates a download link for the fininshed trascript (use md_format())
@app.post("/end")
def end_meeting(user: User):
    

    return {"notes": notes, "download_link": download_link}

# Helper Function
# Inputs blobs and blobs with markdown bulletpoints
def md_format(notes):
    
    return md

# Client asks for download after meeting over
# Check for transcript in processed table
@app.get("/download")
def download_notes(id: str):
    
    return FileResponse(md_file.name, media_type="markdown", filename=fname)
