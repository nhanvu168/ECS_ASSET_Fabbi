from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import AssignSeatSerializers, SeatDetailSerializers
from core.seat.models import SeatModel
from core.employee.models import EmployeeModel
from api.exceptions import ValidationError404, ValidationError400


class SeatAll(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SeatDetailSerializers
    query_set = SeatModel.objects.all()

    def get(self, request):
        serializer = self.serializer_class(self.query_set, many=True)
        return Response(serializer.data)


class SeatDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            seat_obj = SeatModel.objects.get(pk=pk, status=1)
            serializer = SeatDetailSerializers(seat_obj)
            return Response(serializer.data)
        except:
            raise ValidationError404(detail="Seat not found")

    def delete(self, request, pk):
        seat_obj = SeatModel.objects.get(pk=pk, status=1)
        seat_obj.status = 0
        seat_obj.employee = None
        seat_obj.save()
        return Response({"message": "Seat deleted!"}, status=status.HTTP_200_OK)


class AssignSeat(APIView):
    permission_classes = [AllowAny]

    def put(self, request, pk):
        seat = SeatModel.objects.get(seat_id=pk)
        employee_id = seat.employee_id
        if employee_id is None:
            serializer = AssignSeatSerializers(seat, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            raise ValidationError400(detail="The position is already occupied")


