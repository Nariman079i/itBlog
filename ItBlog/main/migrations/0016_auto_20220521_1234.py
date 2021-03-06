# Generated by Django 3.2.13 on 2022-05-21 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_algoritm_alg_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='python',
            name='isOpen',
            field=models.BooleanField(default=False, verbose_name='Доступ к уроку'),
        ),
        migrations.AlterField(
            model_name='python',
            name='test_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.test'),
        ),
    ]
