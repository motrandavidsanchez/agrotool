from rest_framework import serializers

from inventory.models import Tool, Supplies, StaffEquipment


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'


class StaffEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffEquipment
        fields = '__all__'


class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplies
        fields = '__all__'
