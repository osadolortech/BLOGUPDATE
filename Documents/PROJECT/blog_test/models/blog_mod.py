from unicodedata import name
from pydantic import BaseModel

class Blog(BaseModel):
    name: str
    title: str
    content: str

class Comment(BaseModel):
    content: str