# Generated by Django 4.1.6 on 2023-03-01 17:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sur_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='budget',
            field=models.IntegerField(blank=True, default=50000, validators=[django.core.validators.MinValueValidator(10000)]),
        ),
        migrations.AddField(
            model_name='book',
            name='currency',
            field=models.CharField(choices=[('RUB', 'Rubles'), ('USD', 'Dollars'), ('EUR', 'Euro')], default='USD', max_length=3),
        ),
        migrations.AddField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2023)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='book',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book_app.author'),
        ),
    ]
