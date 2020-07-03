# from django.shortcuts.render import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import EndpointInfo, AlgoInfo, AlgoRequest
from .serializers import EndpointInfoSerializer, AlgoInfoSerializer, AlgoRequestSerializer

class EndpointInfoViewSet(RetrieveModelMixin,ListModelMixin,GenericViewSet):
    serializer_class = EndpointInfoSerializer
    queryset = EndpointInfo.objects.all()

class AlgoInfoViewset(RetrieveModelMixin,ListModelMixin,GenericViewSet):
    serializer_class = AlgoInfoSerializer
    queryset = AlgoInfo.objects.all()

class AlgoRequestViewset(RetrieveModelMixin,ListModelMixin,GenericViewSet,UpdateModelMixin):
    serializer_class = AlgoRequestSerializer
    queryset = AlgoRequest.objects.all()

