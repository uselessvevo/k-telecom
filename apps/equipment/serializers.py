import re
from contextlib import suppress
from typing import OrderedDict

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.equipment.models import Equipment, EquipmentType


SERIAL_NUMBER_MASK_MAPPING = {
    'N': '0-9',
    'A': 'A-Z',
    'a': 'a-z',
    'X': 'A-Z|0-9',
    'Z': '-|_|@',
}


def validate_serial_number_mask(serial_number: str, mask: str) -> bool:
    """
    Args:
        serial_number (str): серийный номер
        mask (str): маска серийного номера
    """
    with suppress(AttributeError, IndexError, ValueError):
        if len(serial_number) != len(mask):
            return False
        mask = ''.join(f"{SERIAL_NUMBER_MASK_MAPPING.get(i)}" for i in mask)
        mask = f'[{mask}]+'
        mask_regex = re.compile(mask)
        return True if mask_regex.search(serial_number) else False


class EquipmentTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=125)
    mask = serializers.CharField(max_length=10)

    class Meta:
        model = EquipmentType
        fields = ('id', 'name', 'mask')
        read_only_fields = ('id',)


class EquipmentSerializer(serializers.ModelSerializer):
    # Read/Write attrs
    serial_number = serializers.ListField()
    description = serializers.CharField(required=False)
    equipment_type = EquipmentTypeSerializer(read_only=True)

    # Write only attrs
    mask = serializers.CharField(write_only=True)
    equipment_type_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Equipment
        fields = (
            'id', 'equipment_type', 'equipment_type_id',
            'serial_number', 'description', 'mask'
        )
        read_only_fields = ('id', 'equipment_type')

    def validate(self, attrs) -> OrderedDict:
        """
        На сколько я понял, мы передаём информацию о типе
        оборудования (id, name, mask) и по ним проводим дальнейшую проверку

        Args:
            * serial_number (str): серийный номер
            * name (str): наименование типа оборудования
            * mask (str): маска серийного номера
            * description (str): примечания (не обязательно)
        """
        if Equipment.objects.filter(serial_number=attrs['serial_number']):
            raise ValidationError('Серийный номер уже существует')

        for serial_number in attrs['serial_number']:
            if not validate_serial_number_mask(serial_number, attrs['mask']):
                raise ValidationError(f'Серийный номер "{serial_number}" не прошёл проверку')

        attrs.pop('mask')

        return attrs
