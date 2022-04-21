from django.db import models
from initial_data.models import InitialData as proj_initdata

class InitialData(models.Model):
    project_initdata = models.ForeignKey(
        proj_initdata,
        on_delete=models.CASCADE,
        verbose_name='Выберите запрос'
    )
