from django.db import models


class EmployeeModel(models.Model):
    id = models.CharField(max_length=4, primary_key=True, null=False)
    job_title_code = models.CharField(max_length=32)
    department_code = models.CharField(max_length=32)
    account_id = models.IntegerField(null=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    gender = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employees'
