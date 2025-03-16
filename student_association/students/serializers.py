from rest_framework import serializers
from .models import Discipline, Student, Club, Membership

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'  # Inclut tous les champs du modèle

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    discipline_name = serializers.ReadOnlyField(source='discipline.name')  # Récupère le nom de la discipline

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'discipline', 'discipline_name']

class MembershipSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.first_name')
    club_name = serializers.ReadOnlyField(source='club.name')

    class Meta:
        model = Membership
        fields = ['id', 'student', 'student_name', 'club', 'club_name', 'date_joined']
