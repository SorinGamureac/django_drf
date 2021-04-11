from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedRelatedField, HyperlinkedModelSerializer
from .models import Author, Biography, Book, Article, Project, ToDo

# class AuthorSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Author
#        fields = '__all__'
#
# class BiographySerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Biography
#        fields = ['text', 'author']
#
# class ArticleSerializer(serializers.ModelSerializer):
#    author = AuthorSerializer()
#
#    class Meta:
#        model = Article
#        exclude = ['name']
#
# class BookSerializer(serializers.ModelSerializer):
#    authors = serializers.StringRelatedField(many=True)
#
#    class Meta:
#        model = Book
#        fields = '__all__'

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = '__all__'


class BiographySerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Biography
       fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Article
       fields = '__all__'


class BookSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Book
       fields = '__all__'

class ProjectSerializer(ModelSerializer):
    # Настройка сериализатора
    # Настройка Foreign Key
    owner = HyperlinkedIdentityField(view_name='user-detail')
    # Настройка Many to many
    users = HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    project = HyperlinkedIdentityField(view_name='project-detail')
    creator = HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = ToDo
        exclude = ('is_active',)