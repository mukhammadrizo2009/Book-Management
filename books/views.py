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
        'name': "Odam bo'lish qiyin",
        'author': "O'lmas Umarbekov",
        'publication_year': 2010,
        'status': 'available',
        'isbn': 23442,
    },
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
            return render(request=request , template_name='book_detail.html' , context=context)
    return render(request=request , template_name='book.html')
def add_book_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request , template_name='add_book.html') 
       
    elif request.method == 'POST':
        form = request.POST
        
        print(form)
        
        new_book = {
            'id': 3,
            'name': form.get('name'),
            'author': form.get('author'),
            'publication_year': form.get('publication_year' , 2009),
            'status': form.get('status' , "available"),
            'isbn': form.get('isbn')
        }
        books.append(new_book)
        return redirect(to=reverse('books:books_page'))