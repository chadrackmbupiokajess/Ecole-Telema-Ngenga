from django.urls import path
from . import views

app_name = 'actions'

urlpatterns = [
    # Route pour la liste des actions
    path('', views.action_list, name='actions'),
    # Route pour le détail d'une action (ex: /actions/1/)
    path('<int:pk>/', views.action_detail, name='action_detail'),
]
