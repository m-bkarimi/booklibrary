# book/serializers.py
from rest_framework import serializers
from core.models import Author, Publisher, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        depth = 1
        fields = ('id', 'first_name', 'last_name', 'nickname', )


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'phone', 'address', )


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', )


class BookAuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(source='authors', read_only=True, many=True)  # many=True is required

    class Meta:
        model = Author
        fields = ('books',)


class BookPublisherSerializer(serializers.ModelSerializer):
    books = BookSerializer(source='publishers', read_only=True, many=True)  # many=True is required

    class Meta:
        model = Publisher
        fields = ('books', )
