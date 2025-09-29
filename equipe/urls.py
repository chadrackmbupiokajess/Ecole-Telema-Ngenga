from django.urls import path
from . import views

app_name = 'equipe'

urlpatterns = [
    path('', views.equipe_view, name='equipe'),
]
