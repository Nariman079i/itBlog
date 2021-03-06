# Generated by Django 4.0.2 on 2022-05-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_book_id_alter_book_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='index',
        ),
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='isPublished',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
