from rest_framework import serializers

from plantation.models import Hectare, Batch


class HectareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hectare
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'
