from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import SeatViewSerializers, AssignSeatSerializers, SeatDetail
from api.employee.serializers import StaffAll
from core.seat.models import SeatModel
from core.employee.models import EmployeeModel
from api.exceptions import ValidationError404, ValidationError400


class SeatAll(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SeatViewSerializers
    query_set = SeatModel.objects.all()

    def get(self, request):
        serializer = self.serializer_class(self.query_set, many=True)
        return Response(serializer.data)


class SeatAssigned(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SeatViewSerializers
    query_set = SeatModel.objects.select_related('employee')

    def get(self, request):
        serializer = self.serializer_class(self.query_set, many=True)
        return Response(serializer.data)


class SeatDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            seat_obj = SeatModel.objects.get(pk=pk, is_seat_id_assigned=1)
            serializer = SeatDetail(seat_obj)
            return Response(serializer.data)
        except:
            raise ValidationError404(detail="Seat not found")

    def delete(self, request, pk):
        seat_obj = SeatModel.objects.get(pk=pk, is_seat_id_assigned=True)
        seat_obj.is_seat_id_assigned = False
        seat_obj.employee = None
        seat_obj.save()
        return Response({"message": "Seat deleted!"}, status=status.HTTP_200_OK)


class AssignSeat(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        seat = SeatModel.objects.get(pk=pk, is_seat_id_assigned=False)
        employee_id = seat.employee_id
        if employee_id is None:

            serializer = AssignSeatSerializers(seat, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.is_seat_id_assigned = True
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return ValidationError400(detail="The position is already occupied")
