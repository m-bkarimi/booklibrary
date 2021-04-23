from django.test import Client, TestCase
from django.urls import reverse
from core.models import Book, Author, Publisher


class BookTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
        first_name='Harry Potter',
        last_name='JK Rowling',
        nick_name='25.00',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')