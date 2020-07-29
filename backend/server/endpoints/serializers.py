from rest_framework import serializers
from .models import Symptoms

class SymptomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Symptoms
        fields ='__all__'