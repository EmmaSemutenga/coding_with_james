from django.db import models

# Create your models here.
# Papers Database

# Problem Statement:
# Read publications but sometimes I want to link the papers / books / essays together through keywords.

# Example
# Paper 1 - smartphone language learning. << keyword


# Author(s)
# Link ()
# Keywords/Tags/ (ed-tech, sci-fi, )
# Short description / notes

# (1) A database of papers.
# (2) 

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str: # This arrow is type hinting, it shows you what this method will return. You can delete it.
        return self.name

class Paper(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publication_date = models.CharField(max_length=200)
    CATEGORIES_CHOICES = (
        ('paper', 'paper'),
        ('book', 'book'),
        ('book_chapter', 'book_chapter'),
        ('essay', 'essay'),
    )
    categories = models.CharField(max_length=20, choices=CATEGORIES_CHOICES, default='paper')
    link = models.URLField(blank=True, null=True)
    KEYWORD_CHOICES = (
        ('ed-tech', 'ed-tech'),
        ('novel', 'novel'),
        ('sci-fi', 'sci-fi'),
    )
    keyword = models.CharField(max_length=20, choices=KEYWORD_CHOICES, default='ed-tech')
    notes = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.title
    

