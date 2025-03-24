# Generated by Django 5.1.5 on 2025-03-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('PYTHON', 'Книги по Python'), ('OTHER', 'Другие книги')], default='PYTHON', max_length=10, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to='covers/', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(upload_to='pdfs/', verbose_name='PDF файл'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
