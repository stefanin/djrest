from rest_framework import serializers
from .models import dafare

class dafareSerializer(serializers.Serializer):
    class Meta:
        model= dafare
        fields=['id','titolo','fatto']
