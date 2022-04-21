from iapws import IAPWS97

from initial_data.models import InitialData


def heat_balance(pk):
    all_object_data = InitialData.objects.filter(pk=pk)

    return all_object_data

print(heat_balance(1))
