from pydantic import BaseModel


class User(BaseModel):
    meeting_id: str = ""
    uid: str = ""
    name: str = ""


class TranscriptEntry(BaseModel):
    user: User
    dialogue: str


class Notes(BaseModel):
    notes: str
    download_link: str
