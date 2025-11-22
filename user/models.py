from django.db import models

# Create your models here.
class Book_read(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    GENRES = (
        ('Fiction','Fiction'),
        ('Non-Fiction','Non-Fiction'),
        ('Romance','Romance'),
        ('Science','Science'),
        ('Thriller','Thriller'),
        ('Biography','Biography'),
        ('Self-Help','Self-Help'),
        ('Fantasy','Fantasy'),
        ('Mystery','Mystery'),
        ('Poetry','Poetry')
    )
    genre = models.CharField(max_length=11, choices=GENRES)
    Ratings = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    )
    rating = models.CharField(max_length=1,choices=Ratings)
    date_started = models.DateField()
    date_ended = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/')

class Book_to_read(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    GENRES = (
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Romance', 'Romance'),
        ('Science', 'Science'),
        ('Thriller', 'Thriller'),
        ('Biography', 'Biography'),
        ('Self-Help', 'Self-Help'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Poetry', 'Poetry')
    )
    genre = models.CharField(max_length=11, choices=GENRES)
    cover_image = models.ImageField(upload_to='book_covers/')
    description = models.TextField( blank=True,
        null=True,
        help_text="Provide a detailed description of the item."
    )

class quotes(models.Model):
    quote=models.TextField(
        blank=True,
        null=True,
        help_text="Quote worth remebering is..."
    )
    author = models.CharField(max_length=100)
    book = models.CharField(max_length=100)
