from django.contrib import admin
from .models import Article
# Register your models here.
#admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'year', 'content', 'image')  # Перечисление полей корректное

    list_display = ('title', 'year')  # Поля, которые отображаются в списке статей

    list_filter = ('year',)  # Добавлена запятая для корректного создания кортежа

    search_fields = ('title', 'content')  # Закрыты кавычки
