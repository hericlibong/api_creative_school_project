from rest_framework import serializers
from .models import Discipline, Student, Club

class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'  # Inclut tous les champs du modèle

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    discipline_name = serializers.ReadOnlyField(source='discipline.name')  # Récupère le nom de la 
    clubs = serializers.SlugRelatedField(
        many=True,  # Un étudiant peut avoir plusieurs clubs
        read_only=True,
        slug_field = 'name'  # Récupère les noms des clubs
    )  

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'discipline', 'discipline_name', 'clubs']
