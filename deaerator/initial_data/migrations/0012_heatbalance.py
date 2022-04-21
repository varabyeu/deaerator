# Generated by Django 4.0.4 on 2022-04-21 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('initial_data', '0011_remove_initialdata_is_steam_saturated'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeatBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='initial_data.initialdata')),
            ],
        ),
    ]