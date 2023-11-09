from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from plantation.models import Hectare, Batch
from plantation.v1.serializers import HectareSerializer, BatchSerializer


class HectareViewSet(ListAPIView, viewsets.GenericViewSet):
    queryset = Hectare.objects.all()
    serializer_class = HectareSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']


class BatchViewSet(ListAPIView, viewsets.GenericViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code', 'species', 'objetive']
