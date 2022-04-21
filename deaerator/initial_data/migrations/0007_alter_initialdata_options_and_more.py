# Generated by Django 4.0.4 on 2022-04-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial_data', '0006_alter_initialdata_options_initialdata_steam_pressure'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='initialdata',
            options={'ordering': ('date', 'id')},
        ),
        migrations.AddField(
            model_name='initialdata',
            name='time_water_reserve',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Время запаса воды на период остановки подпитки, ч'),
        ),
    ]
