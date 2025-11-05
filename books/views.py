from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpRequest , HttpResponse

books = [
    {
        'id':1,
        'name': "MEN",
        'author': "Fotih Duman",
        'publication_year': 2023,
        'status': 'available',
        'isbn': 12356,
    },
    {
        'id': 2,
        'name': "Odam bo'lish qiyin"
        'author': "O'lmas Umarbekov"
        'publication_year': 2010,
        'status': 'available',
        'isbn': 23442,
    }
]

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request=request , template_name='home.html')

def books_view(request: HttpRequest) -> HttpResponse:
    context = {
        'books': books,
        'total_books': len(books),
        'available_books': 456,
        'borrowed_books': 889,
        'authors_books': 236
    }
    return render(request=request , template_name='books.html', context=context)

def book_detail_view(request: HttpRequest , book_id: int) -> HttpResponse:
    for book in books:
        if book['id'] == book_id:
            context = {
                'book': book
            }
            return render(request=request , template_name='add_book.html')
        
        elif request.method