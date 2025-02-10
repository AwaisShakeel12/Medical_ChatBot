from django.urls import path
from .import views


urlpatterns = [
    path('api/', views.ask_question, name='ask_question'),
]