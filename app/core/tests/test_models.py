from unittest.mock import patch
from core import models
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.author = models.Author.objects.create(
            first_name='sepris',
            last_name='car'
        )
        cls.publisher = models.Publisher.objects.create(
            name='sepris',
            phone=5664664,
            address='tehran',
        )

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@sepris.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@SEPRIS.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@sepris.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_publisher_str(self):
        """Test the publisher string representation"""
        self.assertEqual(str(self.publisher), self.publisher.name)

    def test_author_str(self):
        """Test the publisher string representation"""
        full_name = f"{self.author.first_name} {self.author.last_name}"
        self.assertEquals(str(self.author), full_name)

    def test_book_str(self):
        """Test the publisher string representation"""
        book = models.Book.objects.create(
            title='sepris rent',
            publisher=self.publisher,
        )

        self.assertEqual(str(book), book.title)

