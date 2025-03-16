import os
import sys
import django

# Ajouter le chemin du projet dans sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Spécifier le module Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_association.settings')

# Initialiser Django
django.setup()

from students.models import Club

def create_clubs():
    clubs = [
        "Club Informatique",
        "Club Sportif",
        "Club Culture & Arts",
        "Club Humanitaire & Écologie",
        "Club Jeux & Stratégie",
    ]

    for club_name in clubs:
        club, created = Club.objects.get_or_create(name=club_name)
        status = "Créé" if created else "Déjà existant"
        print(f"✅ {status} : {club.name}")

if __name__ == "__main__":
    create_clubs()
    print("✅ Tous les clubs ont été ajoutés avec succès !")

