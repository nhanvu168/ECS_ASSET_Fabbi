from rest_framework import serializers
from core.employee.models import EmployeeModel


class StaffAll(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['name', 'department_code', 'job_title_code']


class EmployeeDetail(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    block_id = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeModel
        fields = ['id', 'block_id', 'name', 'department_code', 'job_title_code']
