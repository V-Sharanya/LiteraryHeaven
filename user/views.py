from django.contrib import messages
from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book_read,Book_to_read,quotes

# Create your views here.
def index(request):
    return render(request,'index.html')

def add_book_read(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        rating = request.POST.get("rating")
        date_started = request.POST.get("date_started")
        date_ended = request.POST.get("date_ended")
        cover_image = request.POST.get("cover_image")

        Book_read.objects.create(
            title=title,
            author=author,
            genre=genre,
            rating=rating,
            date_started=date_started,
            date_ended=date_ended,
            cover_image=cover_image
        )

        messages.success(request, "Book has been added successfully!")

    return render(request,'add-book-read.html')

def book_read_list(request):
    books = Book_read.objects.all()
    return render(request,"book-read-list.html",{"books":books})

def books_read_update(request, book_id):
    book = Book_read.objects.get(id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.genre = request.POST.get("genre")
        book.rating = request.POST.get("rating")
        book.date_started = request.POST.get("date_started")
        book.date_ended = request.POST.get("date_ended")
        book.cover_image = request.POST.get("cover_image")

        book.save()

        messages.success(request, "Book updated successfully!")
        return redirect("book-read-list")

    return render(request, "books-read-update.html", {"book": book})

def delete_read_book(request, book_id):
    book = get_object_or_404(Book_read, id=book_id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect("book-read-list")

def add_book_to_read(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        genre = request.POST.get("genre")
        cover_image = request.POST.get("cover_image")
        description = request.POST.get("description")

        Book_to_read.objects.create(
            title=title,
            author=author,
            genre=genre,
            cover_image=cover_image,
            description=description
        )

        messages.success(request, "Book has been added successfully!")

    return render(request,'add-book-to-read.html')

def book_to_read_list(request):
    books = Book_to_read.objects.all()
    return render(request,"books-to-read-list.html",{"books":books})

def books_to_read_update(request, book_id):
    book = Book_to_read.objects.get(id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.genre = request.POST.get("genre")
        book.cover_image = request.POST.get("cover_image")
        book.description = request.POST.get("description")

        book.save()

        messages.success(request, "Book updated successfully!")
        return redirect("book-to-read-list")

    return render(request, "books-to-read-update.html", {"book": book})

def delete_to_read_book(request, book_id):
    book = get_object_or_404(Book_to_read, id=book_id)
    book.delete()
    messages.success(request, "Book deleted successfully!")
    return redirect("book-to-read-list")

def add_quote(request):
    if request.method == "POST":
        quote = request.POST.get("quote")
        author = request.POST.get("author")
        book = request.POST.get("book")
        quotes.objects.create(
            quote=quote,
            author=author,
            book=book
        )
        messages.success(request, "Quote has been added successfully!")

    return render(request, 'quotes-add.html')

def quotes_list(request):
    quote = quotes.objects.all()
    return render(request,"quotes-list.html",{"quote":quote})