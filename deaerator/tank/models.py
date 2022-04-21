from django.db import models


class InitialData(models.Model):
    water_producing = models.PositiveIntegerField(verbose_name='Введите объем деаэратора в м3', default=2)
    hw_temperature = models.PositiveIntegerField(
        verbose_name='Введите температуру питательной вод в град. Цельсия',
        default=70
    )

    def __str__(self):
        return f'Деаэратор атмосферный ДА-{self.water_producing}/{self.hw_temperature}'


# Create your models here.
