from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView

from staff.models import Staff
from staff.v1.serializers import StaffSerializer


class StaffViewSet(ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
