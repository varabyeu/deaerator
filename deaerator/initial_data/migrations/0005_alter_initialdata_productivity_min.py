# Generated by Django 4.0.4 on 2022-04-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial_data', '0004_initialdata_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialdata',
            name='productivity_min',
            field=models.DecimalField(decimal_places=1, default=0.6, max_digits=5, verbose_name='Минимальная производительность'),
        ),
    ]
