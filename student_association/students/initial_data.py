import os
import sys
import django

# Ajouter le chemin du projet dans sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Spécifier le module Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_association.settings')

# Initialiser Django
django.setup()

from students.models import Club, Discipline

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

def create_disciplines():
    disciplines = [
        "Mathématiques", "Informatique", "Physique", "Chimie", "Génie Civil",
        "Génie Électrique", "Génie Mécanique", "Philosophie", "Psychologie",
        "Sociologie", "Histoire", "Géographie", "Sciences Politiques",
        "Littérature Française", "Langues Étrangères", "Linguistique",
        "Journalisme", "Économie", "Gestion des Entreprises", "Marketing",
        "Finance", "Comptabilité", "Médecine", "Pharmacie", "Biologie",
        "Kinésithérapie", "Droit Public", "Droit Privé", "Droit International",
        "Cinéma & Audiovisuel", "Musique", "Théâtre"
    ]

    for discipline_name in disciplines:
        discipline, created = Discipline.objects.get_or_create(name=discipline_name)
        status = "Créé" if created else "Déjà existant"
        print(f"✅ {status} : {discipline.name}")

if __name__ == "__main__":
    create_clubs()
    create_disciplines()
    print("✅ Tous les clubs et disciplines ont été ajoutés avec succès !")

