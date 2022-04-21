# Generated by Django 4.0.4 on 2022-04-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InitialData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_producing', models.PositiveIntegerField(default=2, verbose_name='Введите объем деаэратора в м3')),
                ('hw_temperature', models.PositiveIntegerField(default=70, verbose_name='Введите температуру питательной вод в град. Цельсия')),
            ],
        ),
    ]
