# Generated by Django 4.0.2 on 2022-05-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_test_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='algoritm',
            name='alg_url',
            field=models.ImageField(default=1, upload_to='ico/'),
            preserve_default=False,
        ),
    ]
