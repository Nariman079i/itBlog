# Generated by Django 3.2.13 on 2022-05-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20220521_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='python',
            name='lesson_int',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
