from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Character
from django.db.models import F, Sum, Max, Min, Avg, Count
from django.urls import reverse


# Create your views here.

def test_apps(request):
    books = Book.objects.order_by('title')
    agg = books.aggregate(Max('rating'), Min('rating'), Count('title'))
    return render(request, 'book_app/index.html', {
        'books': books,
        'agg': agg
    })


def one(request, slug_book: str):
    book = get_object_or_404(Book, slug=slug_book)
    return render(request, 'book_app/one_book.html', {
        'number': slug_book,
        'book': book
    })


def all_directors(request):
    directors = Author.objects.all()
    characters = Character.objects.all()
    return render(request, 'book_app/all_dir.html', context={
        'directors': directors,
        'characters': characters,
    })


def one_director(request, number_of_director: id):
    number = get_object_or_404(Author, id=number_of_director)
    return render(request, 'book_app/one_dir.html', context={
        'number': number_of_director,
        'author': number,
    })


def info(request, character_id: id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'book_app/info.html', context={
        'character': character,
        'character_id': character_id
    })
