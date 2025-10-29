from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:id>/', views.delete_book, name='delete_book'),
]
