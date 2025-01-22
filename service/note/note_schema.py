from pydantic import BaseModel


class NoteReq(BaseModel):
    title: str
    content: str
    
class Note(NoteReq):
    id: int
    author: str
    created_at: str
    updated_at: str

class NoteRes(NoteReq):
    id: int
    author: str
    created_at: str
    updated_at: str | None


class NoteListRes(BaseModel):
    cnt: int
    page: int
    limit: int
    notes: list[NoteRes]