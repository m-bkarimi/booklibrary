# book/views.py
from rest_framework import generics
from core.models import Author, Publisher, Book
from .serializers import AuthorSerializer, PublisherSerializer, BookAuthorSerializer,\
                                                                BookPublisherSerializer


class ListAuthor(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ListPublisher(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class DetailBookAuthor(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = BookAuthorSerializer


class DetailBookPublisher(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = BookPublisherSerializer
