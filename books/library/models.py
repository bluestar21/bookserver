from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID_FK = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=40)
    Country = models.CharField(max_length=100)

class Book(models.Model):
    ISBN_PK = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    AuthorID_FK = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.CharField(max_length=40)
    Price = models.CharField(max_length=40)

