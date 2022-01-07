from django.db import models

from core.employee.models import EmployeeModel


class FloorModel(models.TextChoices):
    Tang11 = 'Tầng 11'
    Tang13 = 'Tầng 13'
    Tang14 = 'Tầng 14'
    Tang15 = 'Tầng 15'
    Tang17 = 'Tầng 17'


class SeatModel(models.Model):
    Floor = [
        ('11', 'T11'),
        ('13', 'T13'),
        ('14', 'T14'),
        ('15', 'T15'),
        ('17', 'T17'),
    ]

    seat_id = models.CharField(max_length=4, primary_key=True, null=False)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, related_name='seat')
    block = models.CharField(max_length=10)
    status = models.IntegerField(choices=((0, 'Not assigned'), (1, 'Assigned')), default=0)
    floor = models.CharField(max_length=20, choices=Floor, default='11')

    class Meta:
        indexes = [models.Index(fields=['floor'])]
        db_table = 'seat_employees'
