# Generated by Django 3.1 on 2020-08-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_english_dic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worditem',
            name='word_times',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
