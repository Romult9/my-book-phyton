from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def python_books(request):
    books = Book.objects.filter(category='PYTHON')
    return render(request, 'books/python_books.html', {'books': books})

def other_books(request):
    books = Book.objects.filter(category='OTHER')
    return render(request, 'books/other_books.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Сохраняем email, имя и фамилию
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'books/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на главную страницу после входа
    else:
        form = LoginForm()
    return render(request, 'books/login.html', {'form': form})

def user_logout(request):
    logout(request)  # Выход пользователя
    return redirect('home')  # Перенаправление на главную страницу


