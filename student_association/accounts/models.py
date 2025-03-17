from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    """ 
    Utilisateur de l'API avec un role spécifique
    """
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('student', 'Étudiant'),
        ('manager ', 'Responsable de club'),

    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
