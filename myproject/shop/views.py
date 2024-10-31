from rest_framework import viewsets,permissions
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter
from rest_framework.filters import SearchFilter,OrderingFilter


class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer



class ModelViewSet(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    filter_backends = [DjangoFilterBackend,SearchFilter, OrderingFilter]
    filterset_class = CarFilter
    filterset_fields =['color','price']
    search_fields = ['title_name']
    ordering_fields = ['title_name','price','created_date']
    permission_classes = [permissions.IsAuthenticated]