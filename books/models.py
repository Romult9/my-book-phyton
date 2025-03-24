from django.db import models

# Варианты категорий
CATEGORY_CHOICES = [
    ('PYTHON', 'Книги по Python'),
    ('OTHER', 'Другие книги'),
]

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    cover_image = models.ImageField(upload_to='covers/', verbose_name='Обложка')
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name='PDF файл')
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='PYTHON',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title
