from django.urls import path
from .views import register_view, login_view, logout_view, home_view
from django.urls import path

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
]