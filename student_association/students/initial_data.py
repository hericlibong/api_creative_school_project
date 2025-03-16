import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_association.settings')
django.setup()

from students.models import Club

def create_clubs():
    """
    Crée une liste de clubs prédéfinis et les enregistre dans la base de données s'ils n'existent pas déjà.
    Pour chaque club, la fonction vérifie s'il existe déjà dans la base de données.
    Si le club n'existe pas, il est créé et un message indiquant "Créé" est affiché.
    Si le club existe déjà, un message indiquant "Déjà existant" est affiché.
    """
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
