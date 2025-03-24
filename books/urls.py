from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('python/', views.python_books, name='python_books'),
    path('other/', views.other_books, name='other_books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # Новый маршрут
    path('register/', views.register, name='register'),  # Регистрация
    path('login/', views.user_login, name='login'),  # Вход
    path('logout/', views.user_logout, name='logout'), # Выход
]  
