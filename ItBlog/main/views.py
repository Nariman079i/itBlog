from django.shortcuts import render
from .forms import AddPageForm
from .models import *

def main(requests):
    ul = ['algorithms' ,'pythons' , 'tests' , 'books' ]
    context = {
        'ul': ul
    }
    url_site = 'main/base.html'
    return render(requests , url_site , context=context)

def Addpage(requests):

    if requests.method == "POST":
        form = AddPageForm(requests.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPageForm()

    return render(requests , 'main/add.html' , context={'form' : form})

# python models
def show_pythons(requests):
    context = {
        'lessons':Python.objects.all()
    }
    url_site = 'main/pythons.html'
    return render(requests , url_site , context=context)


def show_python(requests, lesson_id):
    context = {
        'lesson' : Python.objects.filter(pk=lesson_id)
    }
    url_site = 'main/python.html'
    return render(requests, url_site, context=context)

# test models
def show_tests(requests):
    context = {
        'tests' : Test.objects.all()
    }
    url_site = 'main/tests.html'
    return render(requests , url_site , context=context)

def show_test(requests , test_id):
    context = {
        'test' : Test.objects.filter(pk=test_id)
    }
    url_site = 'main/test.html'
    return render(requests , url_site , context=context)

# algorithms models
def show_algorithms(requests):
    context = {
        'algorithms':Algoritm.objects.all()
    }
    url_site = 'main/algorithms.html'
    return render(requests, url_site, context=context )

def show_algorithm(requests , algorithm_id):
    context = {
        'algorithm':Algoritm.objects.filter(pk=algorithm_id)
    }
    url_site = 'main/algorithm.html'
    return render(requests, url_site, context=context )

# book models
def show_books(requests):
    context = {
        'books': Book.objects.all()
    }
    url_site = 'main/books.html'
    return render(requests, url_site , context=context)

def show_book(requests , book_id):
    context = {
        'book' : Book.objects.filter(pk=book_id)
    }
    url_site = 'main/book.html'
    return render(requests, url_site, context=context)

