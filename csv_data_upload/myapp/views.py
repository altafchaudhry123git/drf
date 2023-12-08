from django.shortcuts import render

# Create your views here.
import codecs
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework import serializers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# @api_view(['POST'])
# def import_csv(request):
#     csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         Student.objects.create(
#             name=row['name'],
#             gender=row['gender'],
#             department=row['department'],
#             dob=row['dob'],
#             city=row['city']
#             )
#     return Response('Successfully Uploaded to db!')

# @api_view(['POST','GET'])
# def import_csv(request):
#     csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
#     csv_reader = csv.DictReader(csv_file)    
#     for row in csv_reader:
#         Student.objects.create(
#             name=row['name'],
#             gender=row['gender'],
#             department=row['department'],
#             dob=row['dob'],
#             city=row['city']
#             )
#     return Response('successfully uploaded and saved to db!')

# @api_view(['POST','GET'])
# def other_portal(request):
#     d=Student.objects.all()
#     serializer=StudentSerializer(d, many=True)
#     b=serializer.data
#     print(b)
#     a={'a':1}
#     print(type(b))
#     print(type(a))
#     return Response({'data':serializer.data})
 

#serializer
import rest_framework.serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class FileUpload(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    
    def post(self,request):
        csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csv_file)    
        for row in csv_reader:
            Student.objects.create(
                name=row['name'],
                gender=row['gender'],
                department=row['department'],
                dob=row['dob'],
                city=row['city']
                )
        return Response('successfully uploaded and saved to db!')
    
    def get(self,request):
        d=Student.objects.all()
        serializer=StudentSerializer(d, many=True)
        b={'data':serializer.data}
        return Response(b)
        
            

