
# 🎓 Creative School API (Démo)

Creative School API est une API RESTful construite avec **Django REST Framework**.  
Elle permet de gérer **les étudiants et les clubs** d'une association étudiante avec un **système d'authentification JWT**.

---

## 📌 Fonctionnalités

✔ **Authentification JWT** : Connexion sécurisée via token JWT.  
✔ **Gestion des étudiants** : CRUD complet (**admins uniquement**).  
✔ **Gestion des clubs** : Création, suppression, et assignation d'étudiants (**admins uniquement**).  
✔ **Permissions utilisateur** :  
   - **Admin** → Peut tout faire (CRUD, assignations, voir toutes les données).  
   - **Guest** → Peut seulement **voir les données en lecture seule**.  
✔ **Pagination** : Limite le nombre de résultats affichés par page pour une navigation fluide.

---

## 🚀 Installation et Lancement

### **1️⃣ Cloner le projet**
```bash
git clone https://github.com/ton-utilisateur/creative-school-api.git
cd creative-school-api
```

### **2️⃣ Activer l’environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sous Windows : venv\Scripts\activate
```

### **3️⃣ Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configurer les variables d’environnement**
Un fichier **`.env.sample`** est déjà présent.  
📌 **Copie-le et modifie-le si besoin** :
```bash
cp .env.sample .env
```

### **5️⃣ Lancer le serveur**
```bash
python manage.py runserver
```
📌 **L’API est accessible sur :**  
➡ **`http://127.0.0.1:8000/api/`**

---

## 🔑 **Authentification (JWT)**
L’API utilise **JWT** pour sécuriser l’accès.

### **1️⃣ Obtenir un token JWT**
📍 **Requête :**
```bash
curl.exe -X POST "http://127.0.0.1:8000/api/users/login/" `
         -H "Content-Type: application/json" `
         -d "{""username"": ""admin"", ""password"": ""admin123""}"
```
📍 **Réponse attendue :**
```json
{
    "refresh": "eyJhbGciOiJIUzI1...",
    "access": "eyJhbGciOiJIUzI1..."
}
```
➡ **Le champ `access` contient le token JWT à utiliser dans toutes les requêtes API.** ✅  

### **2️⃣ Utiliser le Token pour accéder aux endpoints**
Dans chaque requête API, ajoute **le token dans le header `Authorization`** :
```bash
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/students/" `
                  -Method GET `
                  -Headers @{"Authorization"="Bearer VOTRE_ACCESS_TOKEN"}
```

### **3️⃣ Rafraîchir un Token Expiré**
Si ton **token expire**, génère-en un nouveau :
```bash
curl.exe -X POST "http://127.0.0.1:8000/api/users/refresh/" `
         -H "Content-Type: application/json" `
         -d "{""refresh"": ""VOTRE_REFRESH_TOKEN""}"
```
📍 **Réponse attendue :**
```json
{
    "access": "NOUVEAU_ACCESS_TOKEN"
}
```
➡ **Utilise ce `access_token` pour continuer à faire des requêtes.**

---

## 📌 **Endpoints API**
📍 **Gestion des étudiants**
| Méthode | Endpoint | Accès | Description |
|---------|----------|------------|-------------|
| `GET` | `/api/students/` | Admin & Guest | Liste des étudiants |
| `POST` | `/api/students/` | Admin uniquement | Ajouter un étudiant |
| `PATCH` | `/api/students/{id}/` | Admin uniquement | Modifier un étudiant |
| `DELETE` | `/api/students/{id}/` | Admin uniquement | Supprimer un étudiant |

📍 **Gestion des clubs**
| Méthode | Endpoint | Accès | Description |
|---------|----------|------------|-------------|
| `GET` | `/api/clubs/` | Admin & Guest | Liste des clubs |
| `POST` | `/api/clubs/` | Admin uniquement | Ajouter un club |
| `PATCH` | `/api/clubs/{id}/` | Admin uniquement | Modifier un club |
| `DELETE` | `/api/clubs/{id}/` | Admin uniquement | Supprimer un club |

📍 **Authentification**
| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `POST` | `/api/users/login/` | Obtenir un token JWT |
| `POST` | `/api/users/refresh/` | Rafraîchir un token expiré |

---

## 📌 **Pagination**
L’API renvoie **5 résultats par page**.
```bash
curl.exe -X GET "http://127.0.0.1:8000/api/students/?page=2" `
         -H "Authorization: Bearer VOTRE_ACCESS_TOKEN"
```
📌 **Permet d’afficher la page 2 des étudiants.**

---

## 📌 **Exemple d’Assignation d’un Étudiant à un Club**
Un **Admin** peut assigner un étudiant à un ou plusieurs clubs :
```bash
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/students/6/" `
                  -Method PATCH `
                  -Headers @{"Content-Type"="application/json"; "Authorization"="Bearer VOTRE_ACCESS_TOKEN"} `
                  -Body "{""clubs"": [1, 3]}"
```
📌 **L’étudiant ID `6` sera assigné aux clubs ayant les IDs `1` et `3`.**

---

## 📌 **Technologies Utilisées**
- Python 3.12
- Django 5.1
- Django REST Framework
- Simple JWT (authentification)
- **SQLite3** (base de données par défaut)

---

## 🎯 **Auteur**
👨‍💻 **Développé par** : [Ton Nom]  
📩 **Contact** : [ton.email@example.com]  
🔗 **GitHub** : [https://github.com/ton-utilisateur](https://github.com/ton-utilisateur)
```

---