from django.db import models

# Create your models here.
class Python(models.Model):

    title = models.CharField("Название" , max_length=30 , null=False)
    ico_url = models.ImageField(upload_to='ico/' , null=False)
    video_url = models.FileField(upload_to='video/' , null=False)
    description = models.TextField("Описание" , null=False)
    isPublished = models.BooleanField("Опубликовано", default=True)
    isOpen = models.BooleanField("Доступ к уроку", default=False)
    lesson_int = models.IntegerField()
    test_id = models.ForeignKey('Test' , on_delete = models.SET_NULL , null=True)


class Test(models.Model):

    title = models.CharField("Название", max_length=30, null=False)
    img_url = models.ImageField(upload_to='img/' , null=False)
    description = models.TextField("Описание" , null=False , default=' ')

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField("Название", max_length=30, null=False)
    author = models.CharField("Автор", max_length=30, null=False)
    url_lit = models.CharField("Ссылка на литрес", max_length=100, null=False)
    book_url = models.FileField("Ссылка на файл", upload_to='books/' , null=True , default=None , blank=True)
    description = models.TextField("Описание" , null=False)
    img = models.ImageField(upload_to='img/' , null=False)
    isPublished = models.BooleanField("Опубликовано" , default=True)

class Algoritm(models.Model):

    title = models.CharField("Название", max_length=30, null=False)
    description = models.TextField("Описание", null=False)
    alg_url = models.ImageField(upload_to='ico/', null=False)
    isPublished = models.BooleanField("Опубликовано", default=True)