from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')  # Поля, отображаемые в списке
    list_filter = ('category',)  # Фильтр по категориям
    search_fields = ('title', 'description')  # Поиск по названию и описанию
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'category')
        }),
        ('Файлы', {
            'fields': ('cover_image', 'pdf_file')
        }),
    )
