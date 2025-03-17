from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    """
    Utilisateur avec 2 types d'accès : admin ou guest.
    """
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('guest', 'Invité'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
