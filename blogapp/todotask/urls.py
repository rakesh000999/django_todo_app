from django.urls import path
from . import views

urlpatterns = [
    path('crud/', views.crud_task), #127.0.0.1/task/crud
    path('single_view/<int:id>', views.single_view),
    path('update/', views.update_task), #127.0.0.1/task/update
    path('delete/<int:id>/', views.delete_view),
]
