# Generated by Django 3.1.1 on 2020-09-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200902_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]