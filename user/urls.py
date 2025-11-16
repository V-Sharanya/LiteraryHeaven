from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add-book-read/',views.add_book_read,name='add-book-read'),
    path('book-read-list/',views.book_read_list,name='book-read-list'),
    path('books_read_update/<int:book_id>/',views.books_read_update,name='books_read_update'),
    path('delete_read_book/<int:book_id>/',views.delete_read_book,name='delete_read_book'),
    path('add-book-to-read/',views.add_book_to_read,name='add-book-to-read'),
    path('book-to-read-list/',views.book_to_read_list,name='book-to-read-list'),
    path('books_to_read_update/<int:book_id>/',views.books_to_read_update,name='books_to_read_update'),
    path('delete_to_read_book/<int:book_id>/',views.delete_to_read_book,name='delete_to_read_book'),
    path('add-quote/',views.add_quote,name='quotes-add'),
    path('quotes-list/',views.quotes_list,name='quotes-list'),
]