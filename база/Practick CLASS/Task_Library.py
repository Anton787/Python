from pydantic import BaseModel

class Book(BaseModel): 
    titel: str
    author: str
    year: int
    is_available: bool

class Library:
    