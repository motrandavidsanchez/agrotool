import datetime

from dateutil.relativedelta import relativedelta
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

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
    filterset_fields = ['code', 'species', 'objetive', 'hectare']

    @action(methods=['get'], detail=True)
    def prune_batch(self, request, pk):
        """
        Endpoint para calcular cuando dias faltan para la poda de Lote
        """
        batch = self.get_object()

        if batch.pruning_date:
            prune_date = batch.pruning_date + relativedelta(years=2)
        else:
            prune_date = batch.planting_date + relativedelta(years=2)

        pruning_days = prune_date - datetime.date.today()

        return Response(
            data={'message': f'Faltan {pruning_days.days} dias para la poda del Lote.'},
            status=status.HTTP_200_OK
        )

