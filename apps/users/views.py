from django.shortcuts import render, redirect
from apps.users.models import User
from apps.books.models import Book, Review
from django.contrib import messages


def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def verify_login(request):
    errors = User.objects.v_login(request.POST)
    print(errors)
    print('8'*80)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('users:login')
    else:
        user = User.objects.get(username=request.POST['username'])
        request.session['user_id'] = user.id
        return redirect('books:books')

def verify_register(request):
    errors = User.objects.v_register(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
    else:
        user = User.objects.create_user(request.POST)
        request.session['user_id'] = user.id
        return redirect('books:books')
    return redirect('users:register')

def user_index(request):
    # print(request.POST['username'])
    if 'user_id' not in request.session:
        return redirect('users:login')
    user = User.objects.get(id=request.session['user_id'])
    # books = Us.user_reviews.all()
    user_books = Book.objects.filter(book_reviews__user__id=user.id)
    print(user_books)
    for book in user_books:
        print(book.title)
    # books = Book.objects.filter(user__username=user.username)
    # print(books)
    #     # for book in books:
    #     print(book['id'])
    context = {
        'books':user_books,
        'f_name':user.f_name,
        'username':user.username,
        'l_name':user.l_name,
    }
    return render(request, 'users/user_index.html', context)

def kill(request):
    request.session.clear()
    return redirect('users:login')

