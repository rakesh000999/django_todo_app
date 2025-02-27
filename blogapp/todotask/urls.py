from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.crud_task),
]
