from django_filters import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields ={
            'marka': ['exact',],
            'color': ['exact',],
            'year': ['exact', ],
            'price': ['gt','lt' ]
        }