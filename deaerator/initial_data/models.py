from django.db import models


class InitialData(models.Model):
    productivity_max = models.DecimalField(
        verbose_name='Необходимая номинальная производительность',
        default=2.0,
        max_digits=5,
        decimal_places=1
    )
    productivity_min = models.DecimalField(
        verbose_name='Необходимая производительность',
        default=0.6,
        max_digits=5,
        decimal_places=1
    )
    water_temperature = models.PositiveIntegerField(
        verbose_name='Температура деаэрации',
        default=70
    )
    date = models.DateField(verbose_name='Дата заполнения', auto_now=True)

    def __str__(self):
        return f'Запрос № {self.id} - атмосферный деаэратор {self.productivity_max} м3/ч от {self.date}'
