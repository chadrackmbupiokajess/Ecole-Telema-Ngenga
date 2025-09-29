from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('a-propos/', views.a_propos, name='a-propos'),
    path('histoire/', views.histoire, name='histoire'),
    path('mission/', views.mission, name='mission'),
]
