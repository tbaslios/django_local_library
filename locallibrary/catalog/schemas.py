from pydantic import BaseModel

class AuthorSchema(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    date_of_death: str

class GenreSchema(BaseModel):
    name: str

class LanguageSchema(BaseModel):
    name: str