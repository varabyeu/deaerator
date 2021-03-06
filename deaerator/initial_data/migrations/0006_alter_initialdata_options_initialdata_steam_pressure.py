# Generated by Django 4.0.4 on 2022-04-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial_data', '0005_alter_initialdata_productivity_min'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='initialdata',
            options={'ordering': ('id', 'date')},
        ),
        migrations.AddField(
            model_name='initialdata',
            name='steam_pressure',
            field=models.DecimalField(decimal_places=2, default=0.4, max_digits=4, verbose_name='Давление пара на деаэрацию в МПа'),
        ),
    ]
