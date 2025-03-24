# Generated by Django 5.1.5 on 2025-03-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(upload_to='covers/')),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
