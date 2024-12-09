# Generated by Django 3.2.16 on 2024-12-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20241208_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание группы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(
                default=1, unique=True, verbose_name='Идентификатор группы'
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(
                default=1, max_length=200, verbose_name='Название группы'
            ),
            preserve_default=False,
        ),
    ]
