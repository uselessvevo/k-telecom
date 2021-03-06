# Generated by Django 4.0.6 on 2022-07-08 09:40

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='description',
            field=models.TextField(verbose_name='Примечания'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='serial_number',
            field=django_mysql.models.ListCharField(models.CharField(default='000000000', max_length=20), max_length=125, size=5),
        ),
    ]
