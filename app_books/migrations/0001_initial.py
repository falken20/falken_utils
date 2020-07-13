# Generated by Django 3.0 on 2020-07-13 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_year', models.IntegerField(max_length=4)),
                ('book_title', models.TextField()),
                ('book_author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_books.AuthorItem')),
            ],
        ),
    ]
