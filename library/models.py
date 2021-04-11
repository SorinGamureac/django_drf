from django.db import models
from usersapp.models import MyUser
from uuid import uuid4

class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.first_name

class Biography(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    text = models.TextField()

class Book(models.Model):
    authors = models.ManyToManyField(Author)
    name = models.CharField(max_length=32, unique=True)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)


class Project(models.Model):
    name = models.CharField(max_length=32, unique=True)
    users = models.ManyToManyField(MyUser)
    repository = models.URLField(blank=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
