# Generated by Django 4.1.6 on 2023-03-07 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_author_book_budget_book_currency_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='sur_name',
            new_name='surname',
        ),
    ]