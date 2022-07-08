from rest_framework import viewsets

from apps.equipment.models import Equipment, EquipmentType
from apps.equipment.serializers import EquipmentSerializer, EquipmentTypeSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    CRUD-контроллер для оборудования
    """
    queryset = Equipment.objects.order_by('-id')
    serializer_class = EquipmentSerializer


class EquipmentTypeViewSet(viewsets.ModelViewSet):
    """
    CRUD-контроллер для вывода списка типов оборудования
    """
    queryset = EquipmentType.objects.order_by('-id')
    serializer_class = EquipmentTypeSerializer
