from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('add/', views.menu_add, name='menu_add'),
    path('update/<int:pk>/', views.menu_update, name='menu_update'),
    path('delete/<int:pk>/', views.menu_delete, name='menu_delete'),
]
