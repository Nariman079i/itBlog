# Generated by Django 4.0.2 on 2022-05-15 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_python_test_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='isPublished',
        ),
    ]