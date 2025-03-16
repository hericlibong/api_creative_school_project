from django.db import models

from django.db import models 

class Discipline(models.Model):
    """ Discipline ou matière de base de l'étudiant (ex: Mathématiques, Physique, etc.) """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    """ Étudiant inscrit dans l'association """
    GENDER_CHOICES = [
        ('M', 'Homme'),
        ('F', 'Femme'),
        ('O', 'Autre'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email}) - {self.discipline.name}"
    
class Club(models.Model):
    """ Club étudiant (ex: Club Informatique, Club Sportif) """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)  # Facultatif

    def __str__(self):
        return self.name

class Membership(models.Model):
    """ Association entre un étudiant et un club """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='memberships')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='memberships')
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'club'], name='unique_student_club')
        ]

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} -> {self.club.name} (Depuis {self.date_joined})"
