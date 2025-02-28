from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'api', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('gestion/', gestion_alumnos, name='gestion')
]