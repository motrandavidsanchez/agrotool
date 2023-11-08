from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from staff.models import Staff
from staff.v1.serializers import StaffSerializer


class StaffViewSet(ListAPIView, viewsets.GenericViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
