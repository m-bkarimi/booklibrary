from django.test import Client, TestCase
from django.urls import reverse
from core.models import Book, Author, Publisher


class BookTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
        first_name='Harry Potter',
        last_name='JK Rowling',
        nickname='JR',
        )
        self.publisher = Publisher.objects.create(
        name='Harry Potter',
        phone=5454,
        address='JR',
        )

    def test_author_listing(self):
        self.assertEqual(f'{self.author.first_name}', 'Harry Potter')
        self.assertEqual(f'{self.author.last_name}', 'JK Rowling')
        self.assertEqual(f'{self.author.nickname}', 'JR')

    def test_publisher_listing(self):
        self.assertEqual(f'{self.publisher.name}', 'Harry Potter')
        self.assertEqual(self.publisher.phone, 5454)
        self.assertEqual(f'{self.publisher.address}', 'JR')
