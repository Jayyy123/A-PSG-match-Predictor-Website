from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name = 'predictor'),
    path('login/',views.loginPage, name='loginPage'),
    path('logoutPage/',views.logoutPage, name='logoutPage'),
    path('prediction/<str:pk>/', views.prediction, name = 'prediction'),
    path('database/', views.database, name = "database"),
    path('signup/', views.signup, name = "signup"),
    path('delete/<str:pk>/', views.delete, name='delete')

]