from rest_framework import serializers
from core.seat.models import SeatModel
from core.employee.models import EmployeeModel
from api.exceptions import ValidationError404, ValidationError400


class AssignSeatSerializers(serializers.ModelSerializer):
    seat_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SeatModel
        fields = ['seat_id', 'employee', 'status']

    def validated(self, data):
        if 'employee' in data:
            employee_id = data['employee']
            if employee_id is not None:
                try:
                    employee = SeatModel.objects.get(employee=employee_id)
                    if employee is not None:
                        raise ValidationError400(detail="Employee had seated")
                except:
                    pass
        return data

    def update(self, instance, validated_data):
        instance.employee_id = validated_data.get('employee', instance.employee_id)
        instance.status = 1
        instance.save()
        return instance


class EmployeeView(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ['id', 'name', 'department_code', 'job_title_code', 'company_code', 'other_email']


class SeatDetailSerializers(serializers.ModelSerializer):
    employee = EmployeeView(many=False)

    class Meta:
        model = SeatModel
        fields = ['seat_id', 'block', 'floor', 'employee']

