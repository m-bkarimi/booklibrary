from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an user address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Publisher(models.Model):
    """Model representing a publisher."""

    class Meta(object):
        db_table = 'publisher'

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Author(models.Model):
    """Model representing an author."""

    class Meta(object):
        db_table = 'author'

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    """Model representing a book."""

    class Meta(object):
        db_table = 'book'

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # Foreign Key used because book can only have one publisher, but publisher can have multiple books
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.PROTECT, related_name='publishers')
    # ManyToManyField used because a author can have many books and a Book can have many author.
    authors = models.ManyToManyField(Author, related_name='authors')
    page_count = models.BigIntegerField(null=True, blank=True)
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
