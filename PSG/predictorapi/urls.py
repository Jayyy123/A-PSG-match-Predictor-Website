from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.listLinks, name = "links"),
    path('create/', views.createPrediction, name = "createPrediction"),
    path('database/', views.database, name = "databaseL"),
    path('delete/', views.delete, name = "deleteL"),
]