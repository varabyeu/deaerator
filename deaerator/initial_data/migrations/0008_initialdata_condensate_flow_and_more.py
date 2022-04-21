# Generated by Django 4.0.4 on 2022-04-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial_data', '0007_alter_initialdata_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='initialdata',
            name='condensate_flow',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, verbose_name='Расход пара вторничного вскипания на деаэратор, т/ч'),
        ),
        migrations.AddField(
            model_name='initialdata',
            name='condensate_temp',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, verbose_name='Температура конденсата, град. Цельсия'),
        ),
        migrations.AddField(
            model_name='initialdata',
            name='second_steam_flow',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5, verbose_name='Расход пара вторничного вскипания на деаэратор, т/ч'),
        ),
        migrations.AddField(
            model_name='initialdata',
            name='second_steam_pressure',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Давление пара вторничного вскипания, МПа'),
        ),
    ]