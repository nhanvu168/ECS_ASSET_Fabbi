from rest_framework import serializers
from core.seat.models import SeatModel
from core.employee.models import EmployeeModel
from api.exceptions import ValidationError404, ValidationError400


class SeatViewSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SeatModel
        fields = ['id', 'block_id', 'position', 'floor', 'employee']


class AssignSeatSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SeatModel
        fields = ['id', 'employee']

    def validated(self, data):
        if 'employee' in data:
            employee = data['employee']
            if employee is not None:
                try:
                    employee = SeatModel.objects.get(employee=employee, floor=floor)
                    if employee is not None:
                        raise ValidationError400(detail="Employee had seated")
                except:
                    pass
        return data

    def update(self, instance, validated_data):
        instance.employee = validated_data.get('employee', instance.employee)
        instance.save()
        return instance


class EmployeeView(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'name', 'department_code', 'job_title_code']


class SeatDetail(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    employees = EmployeeView(many=False)

    class Meta:
        model = SeatModel
        fields = ['id', 'block_id', 'position', 'floor', 'employees']

