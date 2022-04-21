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
    time_water_reserve = models.DecimalField(
        verbose_name='Время запаса воды на период остановки подпитки, ч',
        default=1,
        max_digits=3,
        decimal_places=1
    )
    second_steam_flow = models.DecimalField(
        verbose_name='Расход пара вторничного вскипания на деаэратор, т/ч',
        default=0,
        max_digits=5,
        decimal_places=1
    )
    second_steam_pressure = models.DecimalField(
        verbose_name='Давление пара вторничного вскипания, МПа',
        default=0,
        max_digits=4,
        decimal_places=2
    )
    condensate_flow = models.DecimalField(
        verbose_name='Расход конденсата на деаэратор, т/ч',
        default=0,
        max_digits=5,
        decimal_places=1
    )
    condensate_temp = models.DecimalField(
        verbose_name='Температура конденсата, град. Цельсия',
        default=0,
        max_digits=5,
        decimal_places=1
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
        ordering = ('date', 'id',)
        verbose_name = 'Исходные данные к проекту'
        verbose_name_plural = 'Исходные данные к проекту'


    def condense_state(self):
        """Агрегатное состояние конденсата

        Возвращает состояние конденсата перед деаэратором
        """

        if self.condensate_temp > 100:
            condense_state = 'boiling'
        else:
            condense_state = 'non-boiling'
        return condense_state

    def condense_heat(self):
        return self.condensate_temp * self.condensate_flow / 1000
