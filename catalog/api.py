from ninja import NinjaAPI
from .models import Author, Genre, Language
from .schemas import AuthorSchema, GenreSchema, LanguageSchema
from rest_framework_simplejwt.authentication import JWTAuthentication

api = NinjaAPI(auth=JWTAuthentication()) 

@api.get("/authors/")
def get_authors(request):
    authors = Author.objects.all()
    return authors

@api.get("/authors/{author_id}")
def get_author(request, author_id: int):
    author = Author.objects.get(id=author_id)
    return author

@api.post("/authors/", response=AuthorSchema)
def create_author(request, author: AuthorSchema):
    author_instance = Author.objects.create(**author.dict())
    return {"success": True, "author": author_instance}

@api.put("/authors/{author_id}", response=AuthorSchema)
def update_author(request, author_id: int, author: AuthorSchema):
    author_instance = Author.objects.get(id=author_id)
    for attr, value in author.dict().items():
        setattr(author_instance, attr, value)
    author_instance.save()
    return {"success": True, "author": author_instance}

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author_instance = Author.objects.get(id=author_id)
    author_instance.delete()
    return {"success": True}

@api.get("/genres/")
def get_genres(request):
    genres = Genre.objects.all()
    return genres

@api.post("/genres/", response=GenreSchema)
def create_genre(request, genre: GenreSchema):
    genre_instance = Genre.objects.create(**genre.dict())
    return {"success": True, "genre": genre_instance}

@api.put("/genres/{genre_id}", response=GenreSchema)
def update_genre(request, genre_id: int, genre: GenreSchema):
    genre_instance = Genre.objects.get(id=genre_id)
    for attr, value in genre.dict().items():
        setattr(genre_instance, attr, value)
    genre_instance.save()
    return {"success": True, "genre": genre_instance}

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre_instance = Genre.objects.get(id=genre_id)
    genre_instance.delete()
    return {"success": True}

@api.get("/languages/")
def get_languages(request):
    languages = Language.objects.all()
    return languages

@api.post("/languages/", response=LanguageSchema)
def create_language(request, language: LanguageSchema):
    language_instance = Language.objects.create(**language.dict())
    return {"success": True, "language": language_instance}

@api.put("/languages/{language_id}", response=LanguageSchema)
def update_language(request, language_id: int, language: LanguageSchema):
    language_instance = Language.objects.get(id=language_id)
    for attr, value in language.dict().items():
        setattr(language_instance, attr, value)
    language_instance.save()
    return {"success": True, "language": language_instance}

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language_instance = Language.objects.get(id=language_id)
    language_instance.delete()
    return {"success": True}

