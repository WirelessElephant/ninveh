from django.db.models import Count

from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Book, BookList, Person
from core.serializers import BookSerializer, BookListSerializer, PersonSerializer


class BookFilterSet(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'author__name': ['icontains'],
            'id': ['in']
        }


class PersonFilterSet(filters.FilterSet):
    class Meta:
        model = Person
        fields = {
            'name': ['istartswith'],
            'is_critic': ['exact'], 
            'is_author': ['exact'] 
        }


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilterSet

    @action(detail=False)
    def frequency(self, request):
        requested_count = request.query_params.get('count', None)
        if requested_count is None:
            raise ParseError('You must specify a "count" parameter in the request.')

        target_book_titles = Book.objects\
            .values('title')\
            .annotate(copies=Count('title'))\
            .filter(copies=requested_count)\
            .values_list('title')

        target_books = self.get_queryset().filter(title__in=target_book_titles).distinct('title')
        
        page = self.paginate_queryset(target_books)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(target_books, many=True)
        return Response(serializer.data)



class BookListViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer
    filterset_fields = ['owner', 'books']


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filterset_class = PersonFilterSet

