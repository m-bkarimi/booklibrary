# book/urls.py
from django.urls import path
from .views import ListAuthor, ListPublisher, DetailBookAuthor, DetailBookPublisher
urlpatterns = [
    path('/author/<int:pk>/', DetailBookAuthor.as_view()),
    path('/publisher/<int:pk>/', DetailBookPublisher.as_view()),
    path('/author/', ListAuthor.as_view()),
    path('/publisher/', ListPublisher.as_view()),

]
