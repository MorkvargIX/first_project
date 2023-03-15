from django.contrib import admin
from .models import Book, Author, Character, FeedBack
from django.db.models import QuerySet


# Register your models here.

class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('40-60', 'Средний'),
            ('60<', 'Высокий'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == '40-60':
            return queryset.filter(rating__gte=40).filter(rating__lte=60)
        if self.value() == '60<':
            return queryset.filter(rating__gt=60)


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'rating']


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'gender']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['currency']
    list_display = ['title', 'director', 'rating', 'get_status']
    list_editable = ['director', 'rating']
    ordering = ['-rating']
    list_per_page = 10
    actions = ['set_dollars', 'set_euros']
    search_fields = ['title']
    filter_horizontal = ['actors']
    list_filter = [RatingFilter, ]

    @admin.display(ordering='rating', description='Комментарий')
    def get_status(self, bok):
        if bok.rating < 30:
            return 'Не стоит тратить время'
        if 30 <= bok.rating <= 75:
            return 'Стоит попробовать'
        if bok.rating <= 85:
            return 'Можно почитать'
        return 'Обязательно к прочтению'

    @admin.action(description='Проставить доллары')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Book.USD)

    @admin.action(description='Проставить евро')
    def set_euros(self, request, qs: QuerySet):
        context = qs.update(currency=Book.EUR)
        self.message_user(
            request,
            f'Количество изменений {context}.'
        )
