from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_author(self):
        return reverse('one_dir', args=[self.id])


class Character(models.Model):
    MALE = 'М'
    FEMALE = 'Ж'
    GENDER_CHOICES = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актёр {self.name} {self.surname}'
        return f'Актриса {self.name} {self.surname}'

    def get_actor(self):
        return reverse('character', args=[self.id])


class Book(models.Model):
    RUB = 'RUB'
    USD = 'USD'
    EUR = 'EUR'

    CURRENCY_CHOICES = [
        (RUB, 'Rubles'),
        (USD, 'Dollars'),
        (EUR, 'Euro'),
    ]

    title = models.CharField(max_length=70)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1950), MaxValueValidator(2023)])
    budget = models.IntegerField(blank=True, default=50000, validators=[MinValueValidator(10000)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    is_best_selling = models.BooleanField(default=True)
    director = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    slug = models.SlugField(default='', null=False)
    actors = models.ManyToManyField(Character)

    def __str__(self):
        return f'{self.title} -> рейтинг: {self.rating} -> год: {self.year}'

    def get_book(self):
        return reverse('one_book', args=[self.slug])
