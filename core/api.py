from rest_framework import viewsets

from core.models import Book, BookList, Person
from core.serializers import BookSerializer, BookListSerializer, PersonSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_fields = ['is_author', 'is_critic', 'name']
    search_fields = ['name']