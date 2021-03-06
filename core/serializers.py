from rest_framework import serializers

from core.models import Book, Person, BookList


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.name")
    recommender = serializers.CharField(source="recommender.name")

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'recommender', 'source', 'amazon_link', 'description', 'book_type', 'book_genre', 'book_length')


class BookListSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        many=True, required=False)
    owner = serializers.PrimaryKeyRelatedField(
        queryset=Person.objects.filter(is_critic=True),
        required=True)

    class Meta:
        model = BookList
        fields = '__all__'
