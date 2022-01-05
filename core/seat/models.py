from django.db import models

from api.core.seat import EmployeeModel


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
        ('14', 'T14')
        ('15', 'T15'),
        ('17', 'T17'),
    ]
    id = models.CharField(max_length=4, primary_key=True, null=False)
    employee = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='seat')
    position = models.CharField(max_length=10)
    status = models.BooleanField(default=False, choices=((0, 'No'), (1, 'Yes')))
    floor = models.CharField(max_length=20, choices=Floor, default='11')

    class Meta:
        indexes = [models.Index(fields=['floor'])]
        db_table = 'seat'
