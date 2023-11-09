from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from inventory.models import Tool, StaffEquipment, Supplies
from inventory.v1.serializers import ToolSerializer, StaffEquipmentSerializer, SuppliesSerializer


class ToolViewSet(ListAPIView, viewsets.GenericViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'codigo', 'state']


class StaffEquipmentViewSet(ListAPIView, viewsets.GenericViewSet):
    queryset = StaffEquipment.objects.all()
    serializer_class = StaffEquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'codigo']


class SuppliesViewSet(ListAPIView, viewsets.GenericViewSet):
    queryset = Supplies.objects.all()
    serializer_class = SuppliesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'codigo']

