from django.db import models


class InitialData(models.Model):
    productivity_max = models.DecimalField(
        verbose_name='Необходимая номинальная производительность',
        default=2.0,
        max_digits=5,
        decimal_places=1
    )
    productivity_min = models.DecimalField(
        verbose_name='Минимальная производительность',
        default=0.6,
        max_digits=5,
        decimal_places=1
    )
    water_temperature = models.PositiveIntegerField(
        verbose_name='Температура деаэрации',
        default=70
    )
    steam_pressure = models.DecimalField(
        verbose_name='Давление пара на деаэрацию в МПа',
        default=0.4,
        max_digits=4,
        decimal_places=2
    )
    date = models.DateField(verbose_name='Дата заполнения', auto_now=True)
    notes = models.CharField(
        max_length=255,
        verbose_name='Примечания',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Запрос № {self.id} - атмосферный деаэратор {self.productivity_max} м3/ч от {self.date}'

    class Meta:
        ordering = ('date', 'id', )
