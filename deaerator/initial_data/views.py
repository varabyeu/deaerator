from django.shortcuts import render
from .models import InitialData

def index(request):
    all_objects = InitialData.objects.order_by('date')
    return render(request, 'initial_data/index.html', {
        'title': 'Тепловой расчет деаэратора',
        'all_objects': all_objects
    })
