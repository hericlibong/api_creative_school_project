from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from students.models import Student, Club
from students.serializers import StudentSerializer, ClubSerializer
from accounts.permissions import IsAdmin, IsGuest


class StudentViewSet(ModelViewSet):
    """ API Permettant la gestion des étudiants (CRUD) """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsGuest | IsAuthenticated]
        
        return [permission() for permission in permission_classes]


class ClubViewSet(ModelViewSet):
    """ API Permettant la gestion des clubs (CRUD) """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsGuest | IsAuthenticated]
        
        return [permission() for permission in permission_classes]
