from django.db import models
from django_mysql.models import ListCharField
from model_utils.models import SoftDeletableModel, TimeStampedModel


class EquipmentType(TimeStampedModel, SoftDeletableModel):
    class Meta:
        db_table = 'equipment_types'
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Типы оборудования'

    name = models.CharField('Наименование', max_length=125)
    mask = models.CharField('Маска серийного номера', max_length=10)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (
            f'({self.__class__.__name__}) '
            f'<id: {self.id} '
            f'name: {self.name}'
            f'mask: {self.mask}'
        )


class Equipment(TimeStampedModel, SoftDeletableModel):
    class Meta:
        db_table = 'equipments'
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'
        unique_together = [['equipment_type', 'serial_number']]

    serial_number = ListCharField(
        models.CharField(max_length=20, default='000000000'),
        size=5,
        max_length=125
    )
    description = models.TextField('Примечания', null=True)
    equipment_type = models.ForeignKey(
        to='equipment.EquipmentType',
        null=True,
        on_delete=models.SET_NULL,
        related_name='equipment_types'
    )

    def __str__(self) -> str:
        return self.serial_number

    def __repr__(self) -> str:
        return (
            f'({self.__class__.__name__}) '
            f'<id: {self.id} '
            f'serial_number: {self.serial_number} '
            f'equipment_type: {self.equipment_type.name}>'
        )
