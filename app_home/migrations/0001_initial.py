# Generated by Django 3.1 on 2020-08-28 08:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CountryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherDataItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature data', models.FloatField()),
                ('Rain data', models.FloatField()),
                ('Humidity data', models.FloatField()),
                ('weather_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_home.cityitem')),
            ],
        ),
        migrations.AddField(
            model_name='cityitem',
            name='country_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_home.countryitem'),
        ),
    ]
