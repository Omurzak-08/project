from rest_framework import serializers
from .models import *

class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'




class CarSerializers(serializers.ModelSerializer):
    model = ModelSerializer(read_only=True,many=True)
    class Meta:
        model = Car
        fields = ['title_name','description','marka','model','color', 'volume',
                  'year','type_change', 'image', 'video']

