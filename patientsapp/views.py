from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from.models import Patients
from.serializers import Patientserializers
from rest_framework import status


class hospital_view(APIView):
    def get(self,request):
        queryset = Patients.objects.all()
        serializer_class = Patientserializers(queryset, many=True)
        return Response(serializer_class.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer_class = Patientserializers(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
