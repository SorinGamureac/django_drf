from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author, Project, ToDo, Biography, Book, Article
from .serializers import AuthorSerializer, ProjectSerializer, ToDoSerializer, BiographySerializer, BookSerializer, ArticleSerializer


class AuthorModelViewSets(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BiographyModelViewSets(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer

class BookModelViewSets(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ArticleModelViewSets(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()