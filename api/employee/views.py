from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics
from core.employee.models import EmployeeModel
from .serializers import StaffAll
from rest_framework.permissions import AllowAny


class StaffAll(generics.ListAPIView):
    serializer_class = StaffAll
    query_set = EmployeeModel.objects.all()
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = self.serializer_class(self.query_set, many=True)
        return Response(serializer.data)
