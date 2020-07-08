from rest_framework import serializers

from core.models import Book, Person, BookList


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    owner = PersonSerializer(required=True)

    class Meta:
        model = BookList
        fields = '__all__'