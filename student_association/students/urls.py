from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, ClubViewSet

# Créer un routeur et enregistrer notre API
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'clubs', ClubViewSet)

# Les URLs de notre API
urlpatterns = [
    path('', include(router.urls)),
]