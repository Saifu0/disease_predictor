from rest_framework import serializers
from .models import EndpointInfo, AlgoInfo, AlgoRequest


class EndpointInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndpointInfo
        read_only_fields = ("id","name","created_at")
        fields = read_only_fields

class AlgoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoInfo
        read_only_fields = ("id","name","description","code","version","created_at","parent_endpoint")
        fields = read_only_fields

class AlgoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgoRequest
        read_only_fields = ("id","input_data","full_respone","response","created_at","info")
        fields = ("id","input_data","full_respone","response","response","created_at","info")


















# py -m venv env