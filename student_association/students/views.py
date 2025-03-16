from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student, Club
from .serializers import StudentSerializer, ClubSerializer

class StudentViewSet(ModelViewSet):
    """ API Permettant la gestion des étudiants (CRUD) """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClubViewSet(ModelViewSet):
    """ API Permettant la gestion des clubs (CRUD) """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer