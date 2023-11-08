from rest_framework.routers import DefaultRouter

from inventory.v1.views import ToolViewSet, StaffEquipmentViewSet, SuppliesViewSet
from staff.v1.views import StaffViewSet

router = DefaultRouter()

# Router Inventory
router.register(prefix=r'tools', viewset=ToolViewSet)
router.register(prefix=r'staff_equipament', viewset=StaffEquipmentViewSet)
router.register(prefix=r'supplies', viewset=SuppliesViewSet)

# Router Staff
router.register(prefix=f'staff', viewset=StaffViewSet)
