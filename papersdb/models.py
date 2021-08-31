from django.db import models

# Create your models here.
# Papers Database

# Problem Statement:
# Read publications but sometimes I want to link the papers / books / essays together through keywords.

# Example
# Paper 1 - smartphone language learning. << keyword


# Author(s)
# 
# 
# Categories (paper, book, essay)
# Link ()
# Keywords/Tags/ (ed-tech, sci-fi, )
# Short description / notes

# (1) A database of papers.
# (2) 

class Paper(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.CharField(max_length=200)
    CATEGORIES_CHOICES = (
        ('paper', 'paper'),
        ('book', 'book'),
        ('essay', 'essay'),
    )
    categories = models.CharField(max_length=10, choices=CATEGORIES_CHOICES, default='paper')
    

