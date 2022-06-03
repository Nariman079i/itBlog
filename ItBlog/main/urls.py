from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *
urlpatterns = [
    path('' , main),
    path('add/' , Addpage , name='add'),
    path('books/', show_books),
    path('book/<int:book_id>/', show_book),
    path('pythons/' , show_pythons),
    path('python/<int:lesson_id>/', show_python),
    path('tests/', show_tests),
    path('test/<int:test_id>/', show_test),
    path('algorithms/', show_algorithms),
    path('algorithm/<int:algorithm_id>/', show_algorithm)

        ]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
